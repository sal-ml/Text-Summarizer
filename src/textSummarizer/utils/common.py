import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


# config box allows us to access the dictionary keys as attributes
# ensure annotations is a decorator that checks the type of the arguments and the return type of the function to avoid any runtime errors


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    Read the yaml file and return the ConfigBox object
    
    Args:
    path_to_yaml: Path to the yaml file
    
    Raises:
    BoxValueError: If the yaml file is empty
    e: empty yaml file
    
    Returns:
    ConfigBox: ConfigBox type
    '''
    print(path_to_yaml)
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading yaml file: {path_to_yaml}")
        raise BoxValueError("empty yaml file") from e
    except Exception as e:
        logger.error(f"Error reading yaml file: {path_to_yaml}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directory: list, verbose=True):
    '''
    Create a list of directories
    
    Args:
    path_to_directory: List of paths to the directories
    verbose: Bool, default is True. If True, it will log the directory creation
    '''
    
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    '''
    Get the size of the file in kb
        
        Args:
        path: Path to the file
        
        Returns:
        str: Size of the file in KB
    '''
    size_in_kb = os.path.getsize(path) / 1024
    return f"{size_in_kb:.2f} KB"