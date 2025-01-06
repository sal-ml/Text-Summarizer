from textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = 'Stage 1: Data Ingestion'

try:
    logger.info(f"Running {STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed: {str(e)}")
    raise e

STAGE_NAME = 'Stage 2: Data Validation'

try:
    logger.info(f"Running {STAGE_NAME}")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed: {str(e)}")
    raise e