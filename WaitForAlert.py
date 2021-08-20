from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.NAME,'proceed').click()

wait = WebDriverWait(driver,10)
alert = wait.until(EC.alert_is_present())
print(alert.text)
alert.accept()
driver.quit()