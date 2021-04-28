from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from secrets import USER, PASSWORD
from message import TITLE, BODY
import time

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

PATH = "C:\Program Files\chromedriver.exe"

URL = "https://www.reddit.com/login/"


def login():
    username = driver.find_element_by_xpath('//*[@id="loginUsername"]')
    username.click()
    username.send_keys(USER)

    password = driver.find_element_by_xpath('//*[@id="loginPassword"]')
    password.click()
    password.send_keys(PASSWORD)
    driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()


def open_browser():
    global driver
    driver = webdriver.Chrome(PATH, options=opt, service_log_path='NUL')
    driver.get(URL)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))


open_browser()
login()


class Reddit:
    def __init__(self, url, body, title):
        self.url = url
        self.body = body
        self.title = title
        self.title_xpath = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div/textarea'
        self.title_xpath_alt = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[1]/div/textarea'
        self.body_field_xpath = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div'
        self.body_field_xpath_alt = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div'
        self.post_button_xpath = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div[1]/div[1]/button'
        self.post_button_xpath_alt = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[3]/div[2]/div/div[1]/button'
        self.flair_dropdown_xpath = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[1]/div/button[4]/div'
        self.meme_flair_xpath = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div/div[2]/div[4]/span'
        self.apply_xpath = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[3]/button[1]'

    def create_post(self):
        time.sleep(3)
        driver.get(self.url)
        time.sleep(1)
        try:
            title_field = driver.find_element_by_xpath(self.title_xpath)
            title_field.click()
            title_field.send_keys(self.title)
        except:
            title_field = driver.find_element_by_xpath(self.title_xpath_alt)
            title_field.click()
            title_field.send_keys(self.title)

        try:
            body_field = driver.find_element_by_xpath(self.body_field_xpath)
            body_field.click()
            body_field.send_keys(self.body)
        except:
            body_field = driver.find_element_by_xpath(self.body_field_xpath_alt)
            body_field.click()
            body_field.send_keys(self.body)

        time.sleep(5)
        try:
            post_button = driver.find_element_by_xpath(self.post_button_xpath)
            post_button.click()
        except:
            post_button = driver.find_element_by_xpath(self.post_button_xpath_alt)
            post_button.click()

    def create_post_with_flair(self):
        time.sleep(3)
        driver.get(self.url)
        time.sleep(1)
        try:
            title_field = driver.find_element_by_xpath(self.title_xpath)
            title_field.click()
            title_field.send_keys(self.title)
        except:
            title_field = driver.find_element_by_xpath(self.title_xpath_alt)
            title_field.click()
            title_field.send_keys(self.title)

        try:
            body_field = driver.find_element_by_xpath(self.body_field_xpath)
            body_field.click()
            body_field.send_keys(self.body)
        except:
            body_field = driver.find_element_by_xpath(self.body_field_xpath_alt)
            body_field.click()
            body_field.send_keys(self.body)

        flair_dropdown = driver.find_element_by_xpath(self.flair_dropdown_xpath)
        flair_dropdown.click()
        meme_flair = driver.find_element_by_xpath(self.meme_flair_xpath)
        meme_flair.click()
        apply_flair = driver.find_element_by_xpath()
        apply_flair.click()

        time.sleep(5)
        try:
            post_button = driver.find_element_by_xpath(self.post_button_xpath)
            post_button.click()
        except:
            post_button = driver.find_element_by_xpath(self.post_button_xpath_alt)
            post_button.click()


AllCryptoBets = Reddit("https://www.reddit.com/r/AllCryptoBets/submit", BODY, TITLE)
CryptoMars = Reddit('https://www.reddit.com/r/CryptoMars/submit', BODY, TITLE)
SatoshiBets = Reddit('https://www.reddit.com/r/satoshibets/submit', BODY, TITLE)
CryptoPumping = Reddit('https://www.reddit.com/r/Cryptopumping/submit', BODY, TITLE)
CryptoStreetBets = Reddit('https://www.reddit.com/r/cryptostreetbets/submit', BODY, TITLE)
CryptoMoonCalls = Reddit('https://www.reddit.com/r/cryptomooncalls/submit', BODY, TITLE)
ShitCoinMoonShots = Reddit('https://www.reddit.com/r/shitcoinmoonshots/submit', BODY, TITLE)
MarsWallStreet = Reddit('https://www.reddit.com/r/MarsWallStreet/submit', BODY, TITLE)
CryptoMoon = Reddit('https://www.reddit.com/r/CryptoMoon/submit', BODY, TITLE)
CryptoMoonShots = Reddit('https://www.reddit.com/r/CryptoMoonshots/submit', BODY, TITLE)


def main():
    AllCryptoBets.create_post()
    CryptoMars.create_post()
    SatoshiBets.create_post()
    CryptoPumping.create_post()
    CryptoStreetBets.create_post()
    CryptoMoonCalls.create_post()
    ShitCoinMoonShots.create_post()
    MarsWallStreet.create_post()
    CryptoMoon.create_post()

    # CryptoMoonShots.create_post_with_flair()


if __name__ == '__main__':
    main()
