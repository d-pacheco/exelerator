from .PdfFillerException import PdfFillerException


class NoExcelFilesFoundException(PdfFillerException):
    def __init__(self, data_folder_path: str):
        msg = f"No excel files were found in the data folder: {data_folder_path}"
        super().__init__(f"{msg}")