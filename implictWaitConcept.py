from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

#driver.maximize_window()
# options = webdriver.ChromeOptions()
# options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
# implicite wait applied for all the web element
# This is called global wait
print(driver.title)
driver.get('https://app.hubspot.com/login')

user_name= driver.find_element(By.ID,'username')
user_name.send_keys('test@gmail.com')

#print(dir(webdriver))