import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Continue to set environment variables based on .env values
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
