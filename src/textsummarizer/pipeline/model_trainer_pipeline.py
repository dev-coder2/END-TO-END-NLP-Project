from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.model_trainer import ModelTrainer
from src.textsummarizer.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()