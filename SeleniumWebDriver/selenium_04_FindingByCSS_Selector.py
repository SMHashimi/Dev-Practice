from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name = "detach", value = True)
chrome_driver = webdriver.Chrome(options = chrome_options)

chrome_driver.get("https://www.python.org")
download_link = chrome_driver.find_element(By.CSS_SELECTOR, value = ".download-widget a")
print(download_link.text)

chrome_driver.quit()