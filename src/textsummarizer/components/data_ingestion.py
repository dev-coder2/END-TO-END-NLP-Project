import os
from src.textsummarizer.entity import DataIngestionConfig
from src.textsummarizer.logging  import logger
import zipfile
import urllib.request as request


class DataIngestion:
    
    def __init__(self,config: DataIngestionConfig):
        
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} is downloaded")
        else:
            logger.info(f"files already exists")
            
    def extract_zip_files(self):
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        
    
    
    