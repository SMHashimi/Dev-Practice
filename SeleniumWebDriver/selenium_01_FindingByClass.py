#Why we would use SeleniumWebdriver although we already have beautiful soup.
                                               #- One reason is that you cannot click a button in a website
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_setting = webdriver.ChromeOptions()
chrome_setting.add_experimental_option("detach", True)
setting_driver = webdriver.Chrome(options = chrome_setting )

setting_driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ?ref_=ast_sto_dp&th=1")
INSTANT_POT_PRICE_WHOLE = setting_driver.find_element(By.CLASS_NAME, value = "a-price-whole")
INSTANT_POT_PRICE_FRACTION = setting_driver.find_element(By.CLASS_NAME, value = "a-price-fraction")
print(f"The price is: ${INSTANT_POT_PRICE_WHOLE.text}.{INSTANT_POT_PRICE_FRACTION.text}")

search_bar = setting_driver.find_element(By.NAME, value = "q")
print(search_bar)

setting_driver.quit()