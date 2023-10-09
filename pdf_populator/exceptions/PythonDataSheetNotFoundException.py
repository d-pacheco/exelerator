from .PdfFillerException import PdfFillerException


class PythonDataSheetNotFoundException(PdfFillerException):
    def __init__(self, data_sheet_name: str):
        msg = f"Excel file does not contain sheet name: {data_sheet_name}"
        super().__init__(f"{msg}")