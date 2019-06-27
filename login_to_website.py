from selenium import webdriver

import time

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome()

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

driver.find_element_by_xpath("/html/body/nav/a[3]").click()

# locate email form by_class_name
driver.find_element_by_xpath('//*[@id="username"]').send_keys("neovarun2000@gmail.com")

# sleep for 0.5 seconds
time.sleep(0.5)

# locate password form by_class_name
driver.find_element_by_xpath('//*[@id="password"]').send_keys("testingtesting")

# send_keys() to simulate key strokes

time.sleep(0.5)

# locate submit button by_xpath 
#sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')

# .click() to mimic button click
sign_in_button.click()