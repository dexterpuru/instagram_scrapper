from selenium import webdriver
from time import sleep
from secrets import pw


class Instabot:
    def __init__(self, username, ps):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        # chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("https://www.instagram.com/")
        self.username = username
        sleep(3)
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()
        sleep(2)

    def get_following(self):
        self.driver.find_element_by_xpath(
            "//a[contains(@href, '/{}/')]".format(self.username)).click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "//a[contains(@href, '/following')]").click()
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        with open('following.txt', 'w') as f:
            for item in names:
                f.write("%s\n" % item)
        # print(links)


my_bot = Instabot('dexterpuru', pw)
my_bot.get_following()
