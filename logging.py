import logging


class Logging:
    def __init__(self, name=None, severity=None):

        self.name = name if name is not None else "Logger"

        self.logger = logging.getLogger(self.name)

        if not len(self.logger.handlers):
            self.handler = logging.FileHandler(self.name + ".log")
            self.formatter = logging.Formatter('%(asctime)s %(module)s %(levelname)s: %(message)s')

            self.console_handler = logging.StreamHandler()
            self.console_handler.setFormatter(self.formatter)

            self.handler.setFormatter(self.formatter)
            self.logger.addHandler(self.handler)
            self.logger.addHandler(self.console_handler)

            if (severity is None or severity == "WARNING"):
                self.severity = logging.WARNING
            elif (severity == "DEBUG"):
                self.severity = logging.DEBUG
            else:
                self.severity = logging.INFO

            self.logger.setLevel(self.severity)

    def get_logger(self):
        return self.logger

