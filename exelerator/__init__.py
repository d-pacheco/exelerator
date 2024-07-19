from pathlib import Path


class FolderNames:
    EXCEL_FOLDER_NAME = "data"
    TEMPLATE_FOLDER_NAME = "templates"
    GENERATED_FOLDER_NAME = "generated"


Path(f"./{FolderNames.EXCEL_FOLDER_NAME}/").mkdir(parents=True, exist_ok=True)
Path(f"./{FolderNames.TEMPLATE_FOLDER_NAME}/").mkdir(parents=True, exist_ok=True)
Path(f"./{FolderNames.GENERATED_FOLDER_NAME}/").mkdir(parents=True, exist_ok=True)
