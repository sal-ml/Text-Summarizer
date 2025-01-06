from dataclasses import dataclass
from pathlib import Path

#data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_dir: Path
    unzip_data_dir: Path

#data validation
@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str 
    ALL_REQUIRED_FILES: list