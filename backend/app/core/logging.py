import logging

logger = logging.getLogger("quizkartehai")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.handlers:

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)