import os

from dotenv import load_dotenv

load_dotenv()

RABBIT_MQ_ADDRESS = os.getenv('RABBIT_MQ_ADDRESS')
