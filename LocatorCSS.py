from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.get('https://app.hubspot.com/login')
#driver.find_element(By.CSS_SELECTOR,'#username').send_keys("suhas@gmail.com")
driver.find_element(By.LINK_TEXT,"Sign up").click()