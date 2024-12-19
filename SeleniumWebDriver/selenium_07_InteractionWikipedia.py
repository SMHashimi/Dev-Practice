from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name = "detach", value = True)
chrome_driver = webdriver.Chrome(options = chrome_options)

chrome_driver.get(url = "https://en.wikipedia.org/wiki/Main_Page")

article = chrome_driver.find_element(By.CSS_SELECTOR, value = "#articlecount a")
print(article.text)


chrome_driver.quit()