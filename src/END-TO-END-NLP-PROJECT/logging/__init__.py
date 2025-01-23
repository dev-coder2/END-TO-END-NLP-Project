import os
import sys
import logging 

logging_str="[%(asctime)s: %(levelname)s: %(modules)s: %(message)s]"

log_dir="logs"
log_files_path=os.join.path(log_dir,"continuous_logs.log")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    
    handlers=[
        logging.FileHandler(log_files_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getlogger("summarizerlogger")