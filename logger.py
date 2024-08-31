import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='game.log',
        filemode='w'
    )
    return logging.getLogger('InteractiveLearningGame')

logger = setup_logger()