from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

driver.find_element_by_link_text("Images").click()
driver.implicitly_wait(5)
driver.find_element_by_link_text("Gmail").click()
driver.quit