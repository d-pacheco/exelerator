import logging
import time
from typing import List
from . import FolderNames
from exelerator.exceptions.no_folder_found_exception import NoFolderFoundException
from exelerator.exceptions.no_files_found_exception import NoFilesFoundException
from exelerator.util.config import Config, DefaultConfigKeys
from exelerator.menu_selector import MenuSelector
from exelerator.util.path_helper import PathHelper
from exelerator.wrappers.pdf_wrapper import PdfWrapper
from exelerator.wrappers.workbook_wrapper import WorkbookWrapper

logger = logging.getLogger("exelerator")


class Exelerator:

    def __init__(self, path_helper: PathHelper, config: Config):
        self.path_helper = path_helper
        self.config = config

    def load_workbook(self) -> WorkbookWrapper:
        data_path_base = self.path_helper.find_path(FolderNames.EXCEL_FOLDER_NAME)
        if data_path_base is None:
            raise NoFolderFoundException(FolderNames.EXCEL_FOLDER_NAME)
        excel_files = self.path_helper.load_files_in_folder(data_path_base)
        if not excel_files:
            raise NoFilesFoundException(data_path_base)

        if len(excel_files) == 1:
            excel_file_name = excel_files[0]
            logger.info(f"Only one excel file in data folder. Defaulting to use '{excel_file_name}'")
        else:
            excel_file_name = MenuSelector.select_data_file(excel_files)

        return WorkbookWrapper(
            f"{data_path_base}/{excel_file_name}",
            self.config.GetConfigValue(DefaultConfigKeys.DATA_SHEET_NAME),
        )

    def populate_pdf(self, wb_wrapper: WorkbookWrapper):
        template_path_base = get_template_path_base(self.path_helper)
        template_file_names = get_template_file_names(self.path_helper, template_path_base)
        template_file_name = MenuSelector.select_template_file(template_file_names)
        template_file_path = f"{template_path_base}/{template_file_name}"

        pdf_wrapper = PdfWrapper(template_file_path, self.config)
        for field in pdf_wrapper.get_annotation_fields():
            value = wb_wrapper.get_value_from_key(field)
            if value is None:
                continue
            pdf_wrapper.update_annotation_field(field, value)

        output_pdf_file_name = get_new_pdf_name(wb_wrapper, self.config, template_file_name)
        pdf_wrapper.save_populated_pdf(f"{FolderNames.GENERATED_FOLDER_NAME}/{output_pdf_file_name}")
        logger.info(f"PDF '{output_pdf_file_name}' successfully generated")
        time.sleep(1)


def get_new_pdf_name(wb_wrapper: WorkbookWrapper, config: Config, template_file_name: str):
    client_name = wb_wrapper.get_value_from_key(
        config.GetConfigValue(DefaultConfigKeys.CLIENT_FIELD_NAME))
    if client_name is None:
        client_name = ""
    template_name_lower = template_file_name.lower()
    output_pdf_file_name = template_name_lower.replace("template", client_name)
    return output_pdf_file_name


def get_template_path_base(path_helper: PathHelper) -> str:
    template_path_base = path_helper.find_path(FolderNames.TEMPLATE_FOLDER_NAME)
    if template_path_base is None:
        raise NoFolderFoundException(FolderNames.TEMPLATE_FOLDER_NAME)
    return template_path_base


def get_template_file_names(path_helper: PathHelper, template_path_base: str) -> List[str]:
    template_file_names = path_helper.load_files_in_folder(template_path_base)
    if not template_file_names:
        raise NoFilesFoundException(template_path_base)
    return template_file_names
