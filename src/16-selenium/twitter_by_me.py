from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Twitter:
    def __init__(self, username, password):

        driver_path = "/Users/mustafaakgul/Documents/Apps/BotInstaScripts/include/chromedriver"
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browserProfile.add_argument("--incognito")
        self.browser = webdriver.Chrome(options=self.browserProfile, executable_path=driver_path)
        self.username = username
        self.password = password

    def singIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        #sadece input tag ının xpath ini al
        usernameInput = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        btnSubmit = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")
        btnSubmit.click()

        time.sleep(2)

    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        results = []

        list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")
        time.sleep(2)
        print("count: " + str(len(list)))

        for i in list:
            results.append(i.text)

        print(results)

    def get_followers(self):
        profile_button = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]"
        )
        profile_button.click()
        time.sleep(3)

        followers_button = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a"
        )
        followers_button.click()
        time.sleep(4)

if __name__=="__main__":
    twitter = Twitter(username, password)
    twitter.singIn()
    #twitter.search("python")
    twitter.get_followers()

    #https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-list