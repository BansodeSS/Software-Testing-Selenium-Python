from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="S:\Drivers Testing\chromedriver_win32\chromedriver.exe")
driver.get("https://sangfroidsolutions.com/")

print(driver.title)

driver.get("https://facebook.com/")

print(driver.title)

driver.back()
print(driver.title)

driver.forward()

print(driver.title)

driver.close()