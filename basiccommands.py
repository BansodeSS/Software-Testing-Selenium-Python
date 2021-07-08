import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="S:\Drivers Testing\chromedriver_win32\chromedriver.exe")

driver.get("https://sangfroidsolutions.com/")

driver.find_element_by_xpath("//*[@id='navbar-example']/ul/li[5]/a").click()

time.sleep(5)

#driver.close()

driver.quit()  # closes all tabs