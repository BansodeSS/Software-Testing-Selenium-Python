from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#driver.maximize_window()
driver.get('https://amazon.in')
driver.find_element(By.LINK_TEXT,'Best Sellers').click()
driver.back()
time.sleep(2)
driver.forward()
driver.refresh()
# refreshing 
#driver.find_element(By.XPATH,"//input[@type='submit']").click()
#driver.switch_to.frame(2)
driver.quit()