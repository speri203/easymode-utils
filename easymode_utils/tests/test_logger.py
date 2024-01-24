import pytest
from easymode_utils.logger import LoggerUtils
import logging


@pytest.fixture
def logger_get() -> logging.Logger:
    logger = LoggerUtils().get_logger
    return logger


@pytest.fixture
def init_logger() -> LoggerUtils:
    logger = LoggerUtils()
    return logger


def test_info_log_message(logger_get, caplog) -> None:
    message = "info log"
    log_level = "INFO"
    logger_get.info(message)
    assert message in caplog.text
    assert log_level in caplog.text


def test_get_logger(logger_get) -> None:
    assert isinstance(logger_get, logging.Logger)


def test_change_log_level(init_logger) -> None:
    curr_log_level = init_logger.logger.getEffectiveLevel()
    assert curr_log_level == 10
    new_log_level = logging.INFO
    init_logger.change_log_level(new_log_level)
    curr_log_level = init_logger.logger.getEffectiveLevel()
    assert curr_log_level == 20


#TODO:Figure out where all of the extra handlers are coming from. The length of handlers
#TODO:at this point is at 9 and I am not sure where the extra handlers are coming from.
def test_change_format(init_logger) -> None:
    curr_format = "%(asctime)s - %(levelname)s - %(module)s.%(funcName)s (%(lineno)d): %(message)s"
    assert curr_format == init_logger.get_logger.handlers[2].formatter._fmt
    new_format = "%(message)s"
    init_logger.change_log_format(new_format)
    assert new_format == init_logger.get_logger.handlers[0].formatter._fmt
