from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# # Check for custom log. This will be printed everytime when main.py will be executed.
# logger.info("Welcome to our custom log.")

# Test stage_01_data_ingestion pipeline
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e