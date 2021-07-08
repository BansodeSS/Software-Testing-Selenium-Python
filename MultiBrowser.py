from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="S:\Drivers Testing\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Ie(executable_path="S:\Drivers Testing\IEDriverServer_x64_3.150.1\IEDriverServer.exe")
driver = webdriver.Edge(executable_path="S:\Drivers Testing\edgedriver_win64\msedgedriver.exe")
driver.get("https://sangfroidsolutions.com/")
print(driver.title)
print(driver.page_source)
driver.close()