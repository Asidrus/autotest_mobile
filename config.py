import os
import sys
import logging
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

ENV_LOCAL = '.env_local'
if os.path.isfile(ENV_LOCAL):
    load_dotenv(ENV_LOCAL)

APPIUM_URL = os.getenv("APPIUM_URL", "http://127.0.0.1:4723/wd/hub")
TELEGRAMBOT_IP = os.getenv('TELEGRAMBOT_IP', 'localhost')
TELEGRAMBOT_PORT = os.getenv('TELEGRAMBOT_PORT', 1234)

project_path = os.path.abspath(os.getcwd())
cache_path = project_path + "/../cache"
logs_path = project_path + "/../logs"

# gather the logs
today = datetime.now().date()
fname = autotest_logs + "/" + str(today) + ".log"
if not os.path.exists(fname):
    with open(fname, "w"): pass
logging.basicConfig(filename=fname,
                    format='%(asctime)s|%(levelname)s|%(message)s',
                    level=logging.WARNING,
                    datefmt='%d/%m/%Y %H:%M:%S')
logger = logging
