from typing import List
import logging
from pdfrw import PdfReader, PdfDict, PdfWriter
from exelerator.util.config import Config, DefaultConfigKeys

logger = logging.getLogger("exelerator")


class PdfWrapper:
    def __init__(self, pdf_template_file_path: str, config: Config):
        self.pdf_template = PdfReader(pdf_template_file_path)
        self.config = config
        self.annotation_fields = load_annotation_fields(self.pdf_template)

    def get_annotation_fields(self):
        return self.annotation_fields

    def update_annotation_field(self, field_to_update, value) -> None:
        font_size = self.config.GetConfigValue(DefaultConfigKeys.FONT_SIZE)
        field_updated = False
        for page in self.pdf_template.pages:
            annotations = page['/Annots']
            for annotation in annotations:
                if annotation['/T'] is not None and annotation['/T'] == field_to_update:
                    update_field(annotation, field_to_update, value, font_size)
                    field_updated = True
                elif annotation['/T'] is None and annotation['/Parent']['/T'] == field_to_update:
                    update_field(annotation['/Parent'], field_to_update, value, font_size)
                    field_updated = True

        if not field_updated:
            logger.warning(f"Couldn't find the field {field_to_update} to be updated")

    def save_populated_pdf(self, new_file_path: str):
        PdfWriter().write(new_file_path, self.pdf_template)


def update_field(annotation_to_update, field_to_update, field_value, font_size):
    string_value = str(field_value)
    annotation_to_update.update(PdfDict(
        V=string_value,
        DA=f"/Helv {font_size} Tf 0 g"
    ))
    logger.debug(f"Updated field {field_to_update} with value {string_value}")


def load_annotation_fields(pdf_template: PdfReader) -> List:
    annotation_fields = []
    for page in pdf_template.pages:
        annotations = page['/Annots']
        for annotation in annotations:
            if annotation['/T'] is not None:
                annotation_fields.append(annotation['/T'])
            else:
                parent_annotation = annotation['/Parent']
                if parent_annotation['/T'] is not None:
                    annotation_fields.append(parent_annotation['/T'])
    return annotation_fields
