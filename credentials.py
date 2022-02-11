import os
from dotenv import load_dotenv

load_dotenv()

ENV_LOCAL = '.env_local'
if os.path.isfile(ENV_LOCAL):
    load_dotenv(ENV_LOCAL)

SDO_LOGIN = os.getenv('SDO_LOGIN')
SDO_PASSWORD = os.getenv('SDO_PASSWORD')