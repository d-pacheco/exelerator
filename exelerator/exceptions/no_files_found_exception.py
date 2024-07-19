from .exelerator_exception import ExeleratorException


class NoFilesFoundException(ExeleratorException):
    def __init__(self, folder_path: str):
        msg = f"No files were found in the folder: {folder_path}\n" \
              f"If this is your first time running Excelerator then place your excel and template files,\n" \
              f"in the data and templates folders respectively."
        super().__init__(f"{msg}")
