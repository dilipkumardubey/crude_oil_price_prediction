from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

# # Check for custom log. This will be printed everytime when main.py will be executed.
# logger.info("Welcome to our custom log.")

# Data Ingestion stage
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e


# Data Validation stage
STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e