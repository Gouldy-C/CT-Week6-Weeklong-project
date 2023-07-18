import os
from dotenv import load_dotenv

class Configs:
    load_dotenv()
    SECRET_KEY = os.getenv('SECRET_KEY')