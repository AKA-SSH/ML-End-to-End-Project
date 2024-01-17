# import libraries
import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from source.logger import logging
from source.utilities import save_object
from source.exception import CustomException

# data transformation program
@dataclass
class DataTransformationConfigurations:
    preprocessor_object_file_path= os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_configurations= DataTransformationConfigurations()
    
    def create_data_transformer_object(self):
        """
        This function performs data transformation.
        
        Inputs:
            - numerical columns
            - categorical columns

        Output:
            - preprocessor pipeline

        """
        try:
            # selecting numerical and categorical columns
            num_col= ['writing score', 'reading score']
            cat_col= ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
            
            # creating numerical pipeline
            logging.info('creating numerical pipeline')
            num_pipeline= Pipeline(steps=[('imputer', SimpleImputer(strategy= 'median')),
                                          ('scaler', StandardScaler())])
            logging.info("numerical features' standard scaling completed")
            
            # creating categorical pipeline
            logging.info('creating categorical pipeline')
            cat_pipeline= Pipeline(steps=[('imputer', SimpleImputer(strategy= 'most_frequent')),
                                          ('one_hot_encoder', OneHotEncoder()),
                                          ('scaler', StandardScaler(with_mean= False))])
            logging.info("categorical features' encoding completed")

            # combining num_pipeline and cat_pipeline
            logging.info('combining numerical and categorical pipeline to create preprocessor')
            preprocessor= ColumnTransformer(transformers= [('numerical pipeline', num_pipeline, num_col),
                                                           ('categorical pipeline', cat_pipeline, cat_col)])
            logging.info('preprocessor created')
            
            # return preprocessor
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            # loading data
            logging.info('loading train and test dataset to dataframe')
            train_dataframe= pd.read_csv(train_path)
            test_dataframe= pd.read_csv(test_path)
            logging.info('loading completed')
            
            # preprocessor
            logging.info('loading preprocessor object')
            preprocessor_object= self.create_data_transformer_object()
            logging.info('loading completed')
            target_column= 'math score'
            num_col= ['writing score', 'reading score']
            cat_col= ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
            
            # fetching training columns
            input_features_train_dataframe= train_dataframe.drop(target_column, axis= 1)
            target_feature_train_dataframe= train_dataframe[target_column]

            # fetching testing columns
            input_features_test_dataframe= test_dataframe.drop(target_column, axis= 1)
            target_feature_test_dataframe= test_dataframe[target_column]

            # fitting preprocessor object on train and test data
            logging.info('fitting preprocessor object on train and test data')
            input_features_train_array= preprocessor_object.fit_transform(input_features_train_dataframe)
            input_features_test_array= preprocessor_object.transform(input_features_test_dataframe)
            
            # saving arrays
            train_array= np.c_[input_features_train_array, np.array(target_feature_train_dataframe)]
            test_array= np.c_[input_features_test_array, np.array(target_feature_test_dataframe)]
            logging.info('saved preprocessing object')

            save_object(file_path= self.data_transformation_configurations.preprocessor_object_file_path,
                        obj= preprocessor_object)
            
            return (train_array, 
                    test_array, 
                    self.data_transformation_configurations.preprocessor_object_file_path)

        except Exception as e:
            raise CustomException(e, sys)