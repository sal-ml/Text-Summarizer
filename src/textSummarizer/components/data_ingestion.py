import os
from pathlib import Path
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        ''' 
        downloads the data from the source URL
        '''
        if not os.path.exists(self.config.local_data_dir):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, 
                filename = self.config.local_data_dir)
            logger.info(f"{filename} download! with following information: \n{headers}")
        else:
            logger.info(f"File already exists of size {get_size(Path(self.config.local_data_dir))}")
            
    def unzip_data(self):
        '''
        extracts the zip file to the specified directory
        '''
        unzip_data_dir = self.config.unzip_data_dir
        # create directory if not exists
        os.makedirs(unzip_data_dir, exist_ok=True)
        
        print(self.config.local_data_dir)
        # unzip data
        with zipfile.ZipFile(self.config.local_data_dir, 'r') as zip_ref:
            zip_ref.extractall(unzip_data_dir)
            logger.info(f"Unzipped data at {unzip_data_dir}")