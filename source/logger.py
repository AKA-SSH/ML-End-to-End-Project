import os
import logging
from datetime import datetime

log_path= os.path.join(os.getcwd(), 'logs')
os.makedirs(log_path, exist_ok= True)

log_file= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_file_path= os.path.join(log_path, log_file)

log_level= logging.INFO

logging.basicConfig(filename= log_file_path,
                    format= '%(asctime)s [%(levelname)s] %(name)s - %(message)s',
                    level= log_level)