import pytest
from easymode_utils.logger import LoggerUtils


@pytest.fixture
def setup_logger():
    logger = LoggerUtils().get_logger
    return logger


def test_info_log_message(setup_logger, caplog):
    message = "info log"
    log_level = "INFO"
    setup_logger.info(message)
    assert message in caplog.text
    assert log_level in caplog.text
