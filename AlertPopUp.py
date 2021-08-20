from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#driver.maximize_window()
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.NAME,"proceed").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
#alert.dismiss()
#alert.send_keys()
driver.switch_to.default_content()
time.sleep(3)
driver.quit()