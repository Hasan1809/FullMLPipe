from src.FullMLPipe.config.configuration import ConfigurationManager
from src.FullMLPipe.components.model_trainer import ModelTrainer
from src.FullMLPipe import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config = ConfigurationManager()
        data_validation_config = config.get_model_trainer_config()
        data_validation = ModelTrainer(config = data_validation_config)
        data_validation.train()
        
if __name__ == '__main__':
    try:
        logger.info(f"!!!!!! {STAGE_NAME} is starting !!!!!!")
        obj = ModelTrainingPipeline()
        obj.initiate_model_training()
        logger.info(f"!!!!!! {STAGE_NAME} is over !!!!!!")
    except Exception as e:
        logger.exception(e)
        raise e