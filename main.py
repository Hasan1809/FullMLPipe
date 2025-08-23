from src.FullMLPipe import logger
from src.FullMLPipe.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.FullMLPipe.pipeline.data_validation import DataValidationTrainingPipeline
from src.FullMLPipe.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.FullMLPipe.pipeline.model_trainer import ModelTrainingPipeline




STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"!!!!!! {STAGE_NAME} is starting !!!!!!")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"!!!!!! {STAGE_NAME} is over !!!!!!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"!!!!!! {STAGE_NAME} is starting !!!!!!")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f"!!!!!! {STAGE_NAME} is over !!!!!!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"


try:
    logger.info(f"!!!!!! {STAGE_NAME} is starting !!!!!!")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f"!!!!!! {STAGE_NAME} is over !!!!!!")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"


try:
    logger.info(f"!!!!!! {STAGE_NAME} is starting !!!!!!")
    obj = ModelTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f"!!!!!! {STAGE_NAME} is over !!!!!!")
except Exception as e:
    logger.exception(e)
    raise e