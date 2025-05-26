import logging
import datetime
import os.path


class Logger:
    timestamp = datetime.datetime.now().strftime('%d-%m-%Y___%H-%M-%S')
    LOG_DIR = "Logs"
    LOG_FILE = f'Flight_Booking___{timestamp}.logs'


    @staticmethod
    def get_logger():
        if not os.path.exists(Logger.LOG_DIR):
            os.makedirs(Logger.LOG_DIR)

        logger = logging.getLogger('Logs')
        logger.setLevel(logging.DEBUG)

        log_file = os.path.join(Logger.LOG_DIR, Logger.LOG_FILE)


        File_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        File_handler.setLevel(logging.DEBUG)
        console_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        File_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)


        logger.addHandler(File_handler)
        logger.addHandler(console_handler)

        return logger


logger = Logger.get_logger()
