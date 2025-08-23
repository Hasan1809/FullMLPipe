from src.FullMLPipe.config.configuration import ConfigurationManager
from src.FullMLPipe.components.data_transformation import DataTransformation
from src.FullMLPipe import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt") , 'r') as f:
                all_lines = f.readlines()
                all_true = all(line.strip().endswith('True') for line in all_lines)
            if all_true:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data does not follow the schema")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    try:
        logger.info(f"!!!!!! {STAGE_NAME} is starting !!!!!!")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f"!!!!!! {STAGE_NAME} is over !!!!!!")
    except Exception as e:
        logger.exception(e)
        raise e