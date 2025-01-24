from src.textsummarizer.utlis.common import read_yaml, create_directories
from src.textsummarizer.entity import DataIngestionConfig,DataTransformationConfig
from src.textsummarizer.constant import *
class ConfigurationManager:
    
    def __init__(self,
                 CONFIG_FILE_PATH=CONFIG_FILE_PATH,
                 PARAMS_FILE_PATH=PARAMS_FILE_PATH):
    
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.param=read_yaml(PARAMS_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        root_dir = config.root_dir
        source_URL = config.source_URL
        local_data_file = config.local_data_file
        unzip_dir = config.unzip_dir
        
        return DataIngestionConfig(root_dir=root_dir,source_URL=source_URL,local_data_file=local_data_file,unzip_dir=unzip_dir)
        
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        
        config = self.config.data_transformation
        create_directories([config.root_dir])
        root_dir = config.root_dir
        data_path = config.data_path
        tokenizer_name = config.tokenizer_name
        
        return DataTransformationConfig(root_dir=root_dir, data_path=data_path, tokenizer_name=tokenizer_name)