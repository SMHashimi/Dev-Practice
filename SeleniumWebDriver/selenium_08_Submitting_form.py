from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name = "detach", value = True)
chrome_driver = webdriver.Chrome(options = chrome_options)

#another challenge from our JavaScript course
chrome_driver.get(url = "https://secure-retreat-92358.herokuapp.com/")
fname = chrome_driver.find_element(By.NAME, value = "fName")
lname = chrome_driver.find_element(By.NAME, value = "lName")
email = chrome_driver.find_element(By.NAME, value = "email")
signup = chrome_driver.find_element(By.XPATH, value = '/html/body/form/button')
fname.send_keys("Sayed Mubaris")
lname.send_keys("Hashimi")
email.send_keys("mubaris.hashimi2018@gmail.com")
signup.click()