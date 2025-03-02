# utils.py
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='task_scheduler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

PRIORITY_LEVELS = ['High', 'Medium', 'Low']

def validate_priority(priority):
    if priority not in PRIORITY_LEVELS:
        raise ValueError("Invalid priority level. Choose from: High, Medium, Low.")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
