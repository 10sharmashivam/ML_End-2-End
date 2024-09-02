import logging
import os
from datetime import datetime

# Generate a log file name based on the current date and time
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a path for the logs directory
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# Ensure the logs directory exists
os.makedirs(logs_path,exist_ok=True)

# Full path to the log file
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,     # Path to the log file
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",     # Log message format
    level=logging.INFO,         # Minimum logging level


)

# Example usage:
# logger = logging.getLogger(__name__)
# logger.info("This is an info message")
if __name__ == "__main__":
    logging.info("Logging has started ")  