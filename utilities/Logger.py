import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Users\\anita\\PycharmProjects\\OrangeHRM\\Logs\\OrangeHRM.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger.setLevel(logging.INFO)
        return logger

