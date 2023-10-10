from .PdfFillerException import PdfFillerException


class NoTemplateFolderFoundException(PdfFillerException):
    def __init__(self):
        msg = f"No templates folder could be found"
        super().__init__(f"{msg}")