
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#driver.maximize_window()
driver.get('https://classic.crmpro.com/')
time.sleep(3)
username = driver.find_element(By.NAME,'username')
password = driver.find_element(By.NAME,'password')
submit = driver.find_element(By.XPATH,"//input[@type='submit']")
act_chain = ActionChains(driver)

act_chain.send_keys_to_element(username,'suhas')
act_chain.send_keys_to_element(password,'password')
act_chain.click(on_element=submit)
act_chain.perform()