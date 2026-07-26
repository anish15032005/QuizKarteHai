import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("quizkartehai")
    logger.setLevel(logging.INFO)

    BASE_DIR = Path(__file__).resolve().parents[2]
    LOG_DIR = BASE_DIR / "logs"
    LOG_FILE = LOG_DIR / "application.log"

    LOG_DIR.mkdir(exist_ok=True)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


logger = setup_logger()