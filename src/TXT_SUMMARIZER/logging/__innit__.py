import logging.config
import os
import sys
import logging

# Define the logging format and log directory
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,  
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)  # Log to the console
    ]
)

# Get a logger instance
logger = logging.getLogger("TXT_SUMMARIZERlogger")
logger.setLevel(logging.INFO)
sys.path.append(log_filepath)