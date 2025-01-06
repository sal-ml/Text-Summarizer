from src.textSummarizer.constant import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.textSummarizer.utils.common import read_yaml, create_directories
from pathlib import Path
from src.textSummarizer.entity import DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(self, 
                 config_file_path = CONFIG_FILE_PATH, 
                 params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        return DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source_URL = config.source_URL,
            local_data_dir = Path(config.local_data_dir),
            unzip_data_dir = Path(config.unzip_data_dir)
        )
        
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])
        
        return DataValidationConfig(
            root_dir = Path(config.root_dir),
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILES = config.ALL_REQUIRED_FILES
        )