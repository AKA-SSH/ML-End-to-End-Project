import os
import sys
import dill

import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from source.exception import CustomException

# common utilites
def save_object(file_path, obj):
    try:
        directory_path= os.path.dirname(file_path)
        os.makedirs(directory_path, exist_ok= True)
        with open(file_path, 'wb') as file_object:
            # saving the object in file_object
            dill.dump(obj, file_object)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    y_test_predictions= model.predict(X_test)
    return r2_score(y_test, y_test_predictions)