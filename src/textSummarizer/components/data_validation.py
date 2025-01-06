from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_file_exists(self) -> bool:
        try:
            validation_status = False
            all_files = os.listdir(os.path.join('artifacts', 'data_ingestion', 'samsum_dataset'))
            
            for files in all_files:
                if files not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as file:
                        file.write(f'Validation Status: {validation_status}')
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as file:
                        file.write(f'Validation Status: {validation_status}')
                    
            return validation_status
        except Exception as e:
            logger.error(f"Error in check_data_exists: {str(e)}")
            raise e