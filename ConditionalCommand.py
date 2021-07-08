from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="S:\Drivers Testing\chromedriver_win32\chromedriver.exe")


driver.get("https://facebook.com/")

ele = driver.find_element_by_name("email")
print(ele.is_displayed())

