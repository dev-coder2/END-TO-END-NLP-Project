from src.textsummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textsummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.textsummarizer.logging import logger 

STAGE_NAME="Data Ingestion"

try:
    logger.info(f" Stage Name: {STAGE_NAME}  <<<<<<<<<< initiated >>>>>>>>>>")
    data_ingestion = DataIngestionPipeline
    data_ingestion.initiate_data_ingestion()
    logger.info(f" Stage Name: {STAGE_NAME}  <<<<<<<<<< completed successfully >>>>>>>>>>")
    
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME="Data Transformation"

try:
    logger.info(f" Stage Name: {STAGE_NAME}  <<<<<<<<<< initiated >>>>>>>>>>")
    data_transformation = DataTransformationPipeline()
    data_transformation.initialized_data_transformation()
    logger.info(f" Stage Name: {STAGE_NAME}  <<<<<<<<<< completed successfully >>>>>>>>>>")
    
except Exception as e:
    logger.exception(e)
    raise e 
