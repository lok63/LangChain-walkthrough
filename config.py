from dotenv import load_dotenv, find_dotenv
import openai
from dotenv import load_dotenv
import os

_ = load_dotenv(find_dotenv()) # read local .env file

class Config(object):
    openai.api_key = os.environ['OPENAI_API_KEY']

