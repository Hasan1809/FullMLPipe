from src.FullMLPipe.config.configuration import ConfigurationManager
from src.FullMLPipe.components.model_evaluation import ModelEvaluation
from src.FullMLPipe import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initaite_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
        


if __name__ == "__main__":
    try:
        logger.info(f"!!!!!! {STAGE_NAME} is starting !!!!!!")
        obj = ModelEvaluationPipeline()
        obj.initaite_model_evaluation()
        logger.info(f"!!!!!! {STAGE_NAME} is over !!!!!!")
    except Exception as e:
        logger.exception(e)
        raise e