from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name = "detach", value = True)
chrome_driver = webdriver.Chrome(options = chrome_options)

chrome_driver.get("https://www.python.org")
search_bar = chrome_driver.find_element(By.NAME, value = "q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

chrome_driver.quit()



