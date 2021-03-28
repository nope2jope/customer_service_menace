from BrazenSpeedBot import TestBot
import time
import os

DRIVER_PATH = os.environ['ENV_DRIVER_PATH']

TWITTER_EMAIL = os.environ['ENV_EMAIL']
TWITTER_PASSWORD = os.environ['ENV_PASSWORD']

PLEDGED_UPS = 5
PLEDGED_DOWNS = 100

TWITTER_URL = 'https://www.twitter.com'
SPEED_TEST_URL = 'https://www.speedtest.net/'

tester = TestBot(email=TWITTER_EMAIL, password=TWITTER_PASSWORD, driver=DRIVER_PATH)

test_results = tester.test_connection(test_url=SPEED_TEST_URL)

if test_results[0] < PLEDGED_DOWNS or test_results[1] < PLEDGED_UPS:
    present_downs = test_results[0]
    present_ups = test_results[1]
    alert_message = f'Hey @Xfinity @Comcast. Currently getting {present_downs}MBPS⬇️/{present_ups}MBPS⬆️' \
                    f'in Bellingham, WA despite paying for {PLEDGED_DOWNS}MBPS⬇️/{PLEDGED_UPS}MBPS⬆️' \
                    f'What gives!?'
    tester.alert_provider(tweet_url=TWITTER_URL, message=alert_message)
    time.sleep(5)
    tester.driver.close()
else:
    time.sleep(5)
    tester.driver.close()
    print('Phew! The free market never disappoints!')

