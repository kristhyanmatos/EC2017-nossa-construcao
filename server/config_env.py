import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

URL_DB = os.getenv("URL_DB")
