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
TEMPLATE_BASE_PATH = "/templates"
DATA_BASE_PATH = "/data"

def main():
    VersionManager.isLatestVersion()
    
    template_path_base = PathFinder.findTemplatePath(TEMPLATE_BASE_PATH)
    template_name = MenuSelector.SelectTemplateFile(template_path_base)
    if template_name is None:
        return
    template_file_path = f"{template_path_base}/{template_name}"

    data_path_base = PathFinder.findDataPath(DATA_BASE_PATH)
    excel_name = MenuSelector.SelectDataFile(data_path_base)
    if excel_name is None:
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

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("Exiting...")
    except PdfFillerException as e:
        print(f"An error has occured: {e}")