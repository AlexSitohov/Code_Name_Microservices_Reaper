import os

from dotenv import load_dotenv

load_dotenv()

SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
RABBIT_MQ_ADDRESS = os.getenv('RABBIT_MQ_ADDRESS')
