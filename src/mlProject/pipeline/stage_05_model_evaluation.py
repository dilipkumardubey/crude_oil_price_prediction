
import os
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/dilipkumardubey/crude_oil_price_prediction.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "dilipkumardubey"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "cf8ece7bc6cee01c3cc542f6cbd79e242230c771"

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX==============X")
    except Exception as e:
        logger.exception(e)
        raise e