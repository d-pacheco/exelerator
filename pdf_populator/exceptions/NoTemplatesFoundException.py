from .PdfFillerException import PdfFillerException


class NoTemplatesFoundException(PdfFillerException):
    def __init__(self, template_folder_path: str):
        msg = f"No templates were found in the template folder: {template_folder_path}"
        super().__init__(f"{msg}")