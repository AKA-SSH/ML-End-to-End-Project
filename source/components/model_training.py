# libraries
import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from source.utilities import *
from source.logger import logging
from source.exception import CustomException

# model training program
@dataclass
class ModelTrainingConfiguration:
    trained_model_file_path= os.path.join('artifacts', 'model.pkl')

class  ModelTrainer:
    def __init__(self):
        self.model_trainer_configuration= ModelTrainingConfiguration()

    def initate_model_trainer(self, train_array, test_array):
        try:
            logging.info('splitting train-test data')
            X_train, y_train= train_array[:,:-1], train_array[:,-1]
            X_test, y_test= test_array[:,:-1], test_array[:,-1]
            logging.info('split completed')
            model= LinearRegression()
            logging.info('model under training')
            model_report= evaluate_model(model, X_train, y_train, X_test, y_test)
            logging.info('model trained')
            logging.info('model pickling initiated')
            save_object(file_path= self.model_trainer_configuration.trained_model_file_path,
                        obj= model)
            logging.info('pickling completed')
            return model_report

        except Exception as e:
            raise CustomException(e, sys)