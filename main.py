import pdfrw
import openpyxl

from pdf_populator.util import PathFinder
from pdf_populator.util import MenuSelector
from pdf_populator.util.WorkbookWrapper import WorkbookWrapper
from pdf_populator.util.PdfWrapper import PdfWrapper
from pdf_populator.util.VersionManager import VersionManager
from pdf_populator.exceptions.PdfFillerException import PdfFillerException


DATA_SHEET_NAME = "Python Data"     # The name of sheet in excel that contains the field names and their values
CLIENT_FIELD_NAME = "clientname1_field"
TEMPLATE_FOLDER_NAME = "templates"
EXCEL_FOLDER_NAME = "data"

def main():
    VersionManager.isLatestVersion()
    
    template_path_base = PathFinder.findFolderPath(TEMPLATE_FOLDER_NAME)
    if template_path_base is None:
        print("Could not find templates folder")
        input("Press Enter to exit")
        return
    template_name = MenuSelector.SelectTemplateFile(template_path_base)
    if template_name is None:
        print(f"There are no template files available to select from")
        input("Press Enter to exit")
        return
    template_file_path = f"{template_path_base}/{template_name}"

    data_path_base = PathFinder.findFolderPath(EXCEL_FOLDER_NAME)
    if data_path_base is None:
        print("Could not find data folder")
        input("Press Enter to exit")
        return
    excel_name = MenuSelector.SelectDataFile(data_path_base)
    if excel_name is None:
        print(f"There are no excel files available to select from")
        input("Press Enter to exit")
        return
    excel_file_path = f"{data_path_base}/{excel_name}"

    wb = openpyxl.load_workbook(excel_file_path, data_only=True)
    wb_wrapper = WorkbookWrapper(wb, DATA_SHEET_NAME)
    pdf_template = pdfrw.PdfReader(template_file_path)
    pdf_wrapper = PdfWrapper(pdf_template)

    for field in pdf_wrapper.annotation_fields:
        value = wb_wrapper.GetValueFromKey(field)
        if value is None:
            continue
        pdf_wrapper.UpdateAnnotationField(field, value)
    
    client_name = wb_wrapper.GetValueFromKey(CLIENT_FIELD_NAME)
    if client_name is None:
        client_name = ""
    template_name = template_name.lower()
    output_pdf_file = template_name.replace("template", client_name)
    pdf_wrapper.SavePopulatedPdf(output_pdf_file)
    print(f"PDF {output_pdf_file} successfully generated")
    input("Press Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("Exiting...")
    except PdfFillerException as e:
        print(f"An error has occured: {e}")