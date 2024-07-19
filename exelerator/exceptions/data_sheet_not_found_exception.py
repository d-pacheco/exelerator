from .exelerator_exception import ExeleratorException


class DataSheetNotFoundException(ExeleratorException):
    def __init__(self, data_sheet_name: str):
        msg = f"Excel file does not contain sheet name: {data_sheet_name}\n" \
              f"Please check the configuration 'data_sheet_name' in config.cfg matches " \
              f"the name of your sheet in your excel file"

        super().__init__(f"{msg}")
