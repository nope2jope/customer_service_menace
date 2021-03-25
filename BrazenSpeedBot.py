from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

DRIVER_PATH = os.environ['ENV_DRIVER_PATH']

TWITTER_EMAIL = os.environ['ENV_EMAIL']
TWITTER_PASSWORD = os.environ['ENV_PASSWORD']
TWITTER_URL = 'https://www.twitter.com'
SPEED_TEST_URL = 'https://www.speedtest.net/'

PLEDGED_UPS = 5.0
PLEDGED_DOWNS = 100.0

ALERT_MESSAGE = f'Hey @Xfinity @Comcast. Currently getting {00}MBPS⬇️/{00}MBPS⬆️' \
                f'in Bellingham, WA despite paying for {PLEDGED_DOWNS}MBPS⬇️/{PLEDGED_UPS}MBPS⬆️' \
                f'What gives!?'

class TestBot:
    def __init__(self):
        self.email = TWITTER_EMAIL
        self.password = TWITTER_PASSWORD
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.present_ups = None
        self.present_downs = None

    def test_connection(self, test_url):
        driver = self.driver
        driver.get(test_url)

        time.sleep(5)
        go_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        time.sleep(60)

        downs = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.present_downs = downs.text

        ups = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.present_ups = ups.text

        results = [float(self.present_downs), float(self.present_ups)]
        return results

    def alert_provider(self):
        driver = self.driver
        driver.get(TWITTER_URL)

        # login_button = driver.find_element_by_css_selector('button ')
        # login_button.click()
        time.sleep(5)

        driver.find_element_by_link_text("Log in").click()

        time.sleep(5)

        inputs = driver.find_elements_by_tag_name('input')

        email_input = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email_input.send_keys(self.email)
        #

        pw_input = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pw_input.send_keys(self.password)
        pw_input.send_keys(Keys.RETURN)

        time.sleep(5)

        twitter_field = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]')
        twitter_field.send_keys(ALERT_MESSAGE)



tester = TestBot()

tester.alert_provider()
