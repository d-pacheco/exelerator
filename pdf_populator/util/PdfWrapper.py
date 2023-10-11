import pdfrw
import logging
from .Config import Config
from .Config import DefaultConfigKeys

class PdfWrapper:
    def __init__(self, pdf_template_file_path: str, log: logging.Logger, config: Config):
        self.pdf_template = pdfrw.PdfReader(pdf_template_file_path)
        self.log = log
        self.config = config
        self.pdf_template
        self.annotation_fields = []
        self.LoadAnnotationFields()

    def LoadAnnotationFields(self) -> None:
        for page in self.pdf_template.pages:
            annotations = page['/Annots']
            for annotation in annotations:
                self.annotation_fields.append(annotation['/T'])
        return
    
    def GetAnnotationFields(self):
        return self.annotation_fields

    def UpdateAnnotationField(self, field_to_update, value) -> None:
        for page in self.pdf_template.pages:
            annotations = page['/Annots']
            for annotation in annotations:
                if annotation['/T'] == field_to_update:
                    string_value = str(value)
                    annotation.update(pdfrw.PdfDict(
                        V=string_value, 
                        DA=f"/Helv {self.config.GetConfigValue(DefaultConfigKeys.FONT_SIZE)} Tf 0 g"
                    ))
                    print(f"Updated field {field_to_update} with value {string_value}")
                    self.log.info(f"Updated field {field_to_update} with value {string_value}")
                    return
        print(f"Couldn't find the field {field_to_update} to be updated")
        self.log.warning(f"Couldn't find the field {field_to_update} to be updated")
        return

    def SavePopulatedPdf(self, new_file_name):
        pdfrw.PdfWriter().write(new_file_name, self.pdf_template)
