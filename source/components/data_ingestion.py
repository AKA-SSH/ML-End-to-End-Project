# importing required libraries
import os
import sys
from source.logger import logging
from source.exception import CustomException

import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from source.components.data_transformation import *
from source.components.model_training import *

# data ingestion program
@dataclass
class DataIngestionConfigurations:
    train_data_path:str = os.path.join('artifacts', 'train_data.csv')
    test_data_path:str = os.path.join('artifacts', 'test_data.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_configurations= DataIngestionConfigurations()
    
    def initiate_data_ingestion(self, csv_file_path= 'notebooks\StudentsPerformance.csv'):
        try:
            logging.info('entered data ingestion component')

            # read csv file
            dataframe= pd.read_csv(csv_file_path)
            logging.info('converted dataset into dataframe')

            # creating new directory if not present
            os.makedirs(os.path.dirname(self.ingestion_configurations.train_data_path), exist_ok= True)
            logging.info(f'directory {os.path.dirname(self.ingestion_configurations.train_data_path)} created/touched')
            
            # putting raw data to raw_data_path
            dataframe.to_csv(self.ingestion_configurations.raw_data_path, header=True, index= False)
            logging.info(f'raw data saved to: {self.ingestion_configurations.raw_data_path}')
            
            # splitting the data into train-test data
            logging.info('train-test split initiated')
            train_dataset, test_dataset= train_test_split(dataframe, test_size= 0.2, random_state= 42)
            
            # putting train and test dataset to train_data_path and test_data_path
            train_dataset.to_csv(self.ingestion_configurations.train_data_path, header=True, index= False)
            logging.info(f'train data saved to: {self.ingestion_configurations.train_data_path}')
            test_dataset.to_csv(self.ingestion_configurations.test_data_path, header=True, index= False)
            logging.info(f'test data saved to: {self.ingestion_configurations.test_data_path}')
            logging.info('data ingestion completed')

            # return train and test data paths
            return self.ingestion_configurations.train_data_path, self.ingestion_configurations.test_data_path
        
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == '__main__':
    object= DataIngestion()
    train_dataset, test_dataset= object.initiate_data_ingestion()
    
    data_transformation= DataTransformation()
    train_array, test_array, _= data_transformation.initiate_data_transformation(train_dataset, test_dataset)

    model_trainer= ModelTrainer()
    print(model_trainer.initate_model_trainer(train_array, test_array))