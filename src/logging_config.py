"""
logging_config
"""
import logging


def setup_logging():
    """
    Setup basic logging
    :return:
    """
    logging.basicConfig(
        filename="data/logs.log",
        level=logging.INFO,
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        )
    )
