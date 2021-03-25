from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

DRIVER_PATH = os.environ['ENV_DRIVER_PATH']

TWITTER_USERNAME = os.environ['ENV_USERNAME']
TWITTER_PASSWORD = os.environ['ENV_PASSWORD']

PLEDGED_UPS = 5
PLEDGED_DOWNS = 100


