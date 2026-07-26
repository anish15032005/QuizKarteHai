import logging
from pathlib import Path

logger = logging.getLogger("quizkartehai")
logger.setLevel(logging.INFO)
BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "application.log"
# LOG_FILE = LOG_DIR / "application.log"

# Prevent duplicate handlers
if not logger.handlers:

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    