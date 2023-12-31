import os

from dotenv import load_dotenv

load_dotenv()

RABBIT_MQ_ADDRESS = os.getenv('RABBIT_MQ_ADDRESS')
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
