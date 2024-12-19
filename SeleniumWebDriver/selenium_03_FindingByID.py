from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name = "detach", value = True)
chrome_driver = webdriver.Chrome(options = chrome_options)

chrome_driver.get("https://www.python.org")
button = chrome_driver.find_element(By.ID, value = "submit")
print(button.size)

chrome_driver.quit()


