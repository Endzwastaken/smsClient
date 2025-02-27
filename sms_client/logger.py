import logging


def setup_logger(log_file: str) -> logging.Logger:
    """Настройка логгера."""
    logger = logging.getLogger('sms_client')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
