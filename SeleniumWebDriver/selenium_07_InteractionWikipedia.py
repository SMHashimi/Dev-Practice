from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name = "detach", value = True)
chrome_driver = webdriver.Chrome(options = chrome_options)

chrome_driver.get(url = "https://en.wikipedia.org/wiki/Main_Page")

article = chrome_driver.find_element(By.CSS_SELECTOR, value = "#articlecount a")
# article.click()

all_portals = chrome_driver.find_element(By.LINK_TEXT, value = "Content portals")
# all_portals.click()

search = chrome_driver.find_element(By.NAME, value = "search")
search.send_keys("Chase Bank")
search.send_keys(Keys.ENTER)








