
from src.textsummarizer.components.data_ingestion import DataIngestion
from src.textsummarizer.config.configuration import ConfigurationManager

class DataIngestionPipeline:
    
    def __init__(self):
        
        pass
    
    def initiate_data_ingestion():
        
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion_func = DataIngestion(config=data_ingestion_config)
        data_ingestion_func.download_file()
        data_ingestion_func.extract_zip_files()
        