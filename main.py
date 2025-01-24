from src.textsummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textsummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.textsummarizer.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.textsummarizer.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline
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

STAGE_NAME="Model Trainer stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
