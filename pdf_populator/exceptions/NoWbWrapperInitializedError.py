from .PdfFillerException import PdfFillerException


class NoWbWrapperInitializedError(PdfFillerException):
    def __init__(self, msg: str = None):
        if msg is None:
            msg = f"No Workbook wrapper initialized."
        super().__init__(f"{msg}")