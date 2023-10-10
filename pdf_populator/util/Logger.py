import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

FILE_SIZE = 1024 * 1024 * 100  # 100 MB
BACKUP_COUNT = 5  # keep up to 5 files


class Logger:
    @staticmethod
    def create_logger(debug: bool):
        if debug:
            level = logging.DEBUG
        else:
            level = logging.WARNING
        
        Path("./logs/").mkdir(parents=True, exist_ok=True)
        log_path = "./logs/pdf_populator.log"
        file_handler = RotatingFileHandler(
            log_path,
            mode="a+",
            maxBytes=FILE_SIZE,
            backupCount=BACKUP_COUNT,
            encoding='utf-8'
        )

        logging.basicConfig(
            format="%(asctime)s %(levelname)s: %(message)s",
            level=level,
            handlers=[file_handler],
        )
        log = logging.getLogger("PDF Populator")
        return log