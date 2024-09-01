import logging
import sys
from config import config

def setup_logger():
    logger = logging.getLogger('InteractiveLearningGame')
    log_level = getattr(logging, config.log_level.upper())
    logger.setLevel(log_level)

    # Erstellen Sie einen FileHandler
    file_handler = logging.FileHandler('game.log', mode='w')
    file_handler.setLevel(logging.DEBUG)

    # Erstellen Sie einen StreamHandler für die Konsolenausgabe
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # Erstellen Sie ein Formatter-Objekt
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Fügen Sie die Handler zum Logger hinzu
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()