from .PdfFillerException import PdfFillerException


class NoPdfWrapperInitializedError(PdfFillerException):
    def __init__(self, msg: str = None):
        if msg is None:
            msg = f"No PDF wrapper initialized."
        super().__init__(f"{msg}")