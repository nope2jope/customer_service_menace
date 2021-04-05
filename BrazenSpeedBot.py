from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestBot:
    def __init__(self, email, password, driver):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(driver)
        self.present_ups = None
        self.present_downs = None

    def test_connection(self, test_url):
        driver = self.driver
        driver.get(test_url)
        
        # sleeping helps assure driver can find element
        # also helps to not look too much like a bot
        time.sleep(5)
       
        go_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        
        # conntection test shouldn't take longer than a minute to run, with a lil padding for above reason too
        time.sleep(60)

        downs = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.present_downs = downs.text

        ups = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.present_ups = ups.text

        time.sleep(5)

        results = [float(self.present_downs), float(self.present_ups)]
        return results

    def alert_provider(self, tweet_url, message):
        driver = self.driver
        driver.get(tweet_url)

        time.sleep(5)

        driver.find_element_by_link_text("Log in").click()

        time.sleep(5)

        email_input = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email_input.send_keys(self.email)

        pw_input = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pw_input.send_keys(self.password)
        
        # sending RETURN is a convenient alternative to locating an element
        pw_input.send_keys(Keys.RETURN)

        time.sleep(5)

        # cumberson xpath, but interactive/keys-sendable input box can be difficult to locate by css
        bird_box = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        bird_box.click()
        bird_box.send_keys(message)

        tweet_button = driver.find_element_by_xpath('//*[@data-testid="tweetButtonInline"]')

        time.sleep(5)

        tweet_button.click()

        ### driver is not closed in this function ###
        
