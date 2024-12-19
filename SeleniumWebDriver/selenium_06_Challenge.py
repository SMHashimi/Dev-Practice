from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name = "detach", value = True)
chrome_driver = webdriver.Chrome(options = chrome_options)

chrome_driver.get(url = "https://www.python.org")

event_times = chrome_driver.find_elements(By.CSS_SELECTOR, value = ".event-widget time")
event_names = chrome_driver.find_elements(By.CSS_SELECTOR, value = ".event-widget ul a")

dict = {}
for item in range(0, len(event_names)):
    dict[item] = {
        "time": event_times[item].text,
        "name": event_names[item].text,
    }
print(dict)

chrome_driver.quit()




