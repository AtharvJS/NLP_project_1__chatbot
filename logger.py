import logging
import datetime
import time
import os
import pytz # You'll need to install this: pip install pytz

# --- Custom IST Timezone Converter ---
def ist_time(*args):
    """
    Converts a timestamp to Indian Standard Time (IST).
    UTC offset for IST is +5:30.
    """
    utc_dt = datetime.datetime.utcnow()
    ist_offset = datetime.timedelta(hours=5, minutes=30)
    ist_dt = utc_dt + ist_offset
    return ist_dt.timetuple()

# --- Log File Setup ---
# Define the Indian timezone for log file naming
indian_timezone = pytz.timezone('Asia/Kolkata')

# Generate the log file name with IST timestamp
# e.g., "13 June 2025 at 08:00 PM.log"
log_file_name = f"{datetime.datetime.now(indian_timezone).strftime('%d %B %Y at %I:%M %p')}.log"

# Define the directory where logs should be stored
# This will create a 'logs' folder in your current working directory
log_directory = os.path.join(os.getcwd(), 'logs')

# Create the log directory if it doesn't exist
os.makedirs(log_directory, exist_ok=True)

# Combine the log directory and the log file name to get the full path
log_file_path = os.path.join(log_directory, log_file_name)

# --- Logging Configuration ---
# 1. Get a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # Set the minimum logging level

# 2. Create a console handler (for printing to the console)
console_handler = logging.StreamHandler()

# 3. Create a file handler (for writing to the log file)
# The 'a' mode means append, so new messages are added to the end of the file
file_handler = logging.FileHandler(log_file_path, mode='a')

# 4. Create a formatter with your desired format string
# This formatter will be used for both console and file output
formatter = logging.Formatter(
    fmt='[%(asctime)s]: %(message)s:',
    datefmt='%Y-%m-%d %H:%M:%S' # Format for the timestamp within the log message
)

# 5. Set the custom IST converter for the formatter
formatter.converter = ist_time

# 6. Apply the formatter to both handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 7. Add both handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# --- Example Usage ---
# logger.info("This is an INFO message, visible on console and in log file.")
# time.sleep(0.5)
# logger.warning("A warning message, also going to both destinations.")
# logger.debug("This debug message won't be shown because level is INFO.")

# print(f"\nLog messages written to console and also to: {log_file_path}")
# print(f"Check the 'logs' folder in your current directory.")