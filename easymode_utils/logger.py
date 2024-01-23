import logging


class LoggerUtils:
    def __init__(self) -> None:
        """
        Initializes the LoggerUtils class with a logger and a stream handler.

        Args:
            args (dict): A dictionary that contains configuration for the logger.
                         It should have a 'module_name' key to set the logger's name.
                         If not provided, 'default_module' is used.
        """
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        self.stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime) - %(levelname)s - %(module)s.%(funcName)s (%(lineno)d): %(message)s"
        )
        self.stream_handler.setFormatter(formatter)
        self.logger.addHandler(self.stream_handler)

    @property
    def get_logger(self) -> logging.Logger:
        """
        Returns the logger instance.

        Returns:
            logging.Logger: The logger instance.
        """
        return self.logger

    def change_log_level(self, log_level: int) -> None:
        """
        Changes the log level of the logger and the stream handler.

        Args:
            log_level (int): The new log level to set. It should be one of the
                             logging level constants defined in the logging module.

        Returns:
            None
        """
        self.logger.setLevel(log_level)
        self.stream_handler.setLevel(log_level)

    def change_log_format(self, format: str) -> None:
        """
        Changes the log format of the stream handler.

        Args:
            format (str): The new log format to set. It should be a string that
                          defines the log format.

        Returns:
            None
        """
        formatter = logging.Formatter(format)
        self.stream_handler.setFormatter(formatter)


# def main():
#     logger = LoggerUtils().get_logger
#     logger.debug("This is a debug message")
#     logger.info("This is an info message")
#     logger.warning("This is a warning message")
#     logger.error("This is an error message")
#     logger.critical("This is a critical message")
#
#
# main()
