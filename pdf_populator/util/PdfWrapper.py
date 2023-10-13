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
                if annotation['/T'] != None:
                    self.annotation_fields.append(annotation['/T'])
                else:
                    parent_annotation = annotation['/Parent']
                    if parent_annotation['/T'] != None:
                        self.annotation_fields.append(parent_annotation['/T'])
        return
    
    def GetAnnotationFields(self):
        return self.annotation_fields

    def UpdateAnnotationField(self, field_to_update, value) -> None:
        for page in self.pdf_template.pages:
            annotations = page['/Annots']
            for annotation in annotations:
                if annotation['/T'] != None and annotation['/T'] == field_to_update:
                    self.UpdateAnnotationFieldHelper(annotation, field_to_update, value)
                    return
                elif annotation['/T'] == None and annotation['/Parent']['/T'] == field_to_update:
                    self.UpdateAnnotationFieldHelper(annotation['/Parent'], field_to_update, value)

        print(f"Couldn't find the field {field_to_update} to be updated")
        self.log.warning(f"Couldn't find the field {field_to_update} to be updated")
        return

    def SavePopulatedPdf(self, new_file_name):
        pdfrw.PdfWriter().write(new_file_name, self.pdf_template)

    def UpdateAnnotationFieldHelper(self, annotation_to_update, field_to_update, field_value):
        string_value = str(field_value)
        annotation_to_update.update(pdfrw.PdfDict(
            V=string_value, 
            DA=f"/Helv {self.config.GetConfigValue(DefaultConfigKeys.FONT_SIZE)} Tf 0 g"
        ))
        print(f"Updated field {field_to_update} with value {string_value}")
        self.log.info(f"Updated field {field_to_update} with value {string_value}")