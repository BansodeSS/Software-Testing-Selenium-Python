from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#driver.maximize_window()
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')
driver.find_element(By.NAME,'upfile').send_keys('C:\\Users\\Sangfroid Solutions\\Downloads\\day1.ipynb')

driver.find_element(By.XPATH,"//input[@type='submit']").click()
#driver.switch_to.frame(2)
driver.quit()