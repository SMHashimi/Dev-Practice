from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name = "detach", value = True)
chrome_driver = webdriver.Chrome(options = chrome_options)

chrome_driver.get("https://www.python.org")
text_latest = chrome_driver.find_element(By.XPATH, value = '//*[@id="content"]/div/section/div[2]/div[2]/p[2]')
text_latest_list = text_latest.text.split(":")
print(f"{text_latest_list[0]}:")

chrome_driver.quit()