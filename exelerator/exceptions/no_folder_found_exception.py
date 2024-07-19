from .exelerator_exception import ExeleratorException


class NoFolderFoundException(ExeleratorException):
    def __init__(self, folder_name: str):
        msg = f"No {folder_name} folder could be found"
        super().__init__(f"{msg}")
