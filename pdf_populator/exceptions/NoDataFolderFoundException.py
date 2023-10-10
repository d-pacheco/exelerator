from .PdfFillerException import PdfFillerException


class NoDataFolderFoundException(PdfFillerException):
    def __init__(self):
        msg = f"No data folder could be found"
        super().__init__(f"{msg}")