from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://app.hubspot.com/login')
wait = WebDriverWait(driver,100)
email = wait.until(EC.presence_of_element_located((By.ID,'username')))
email.send_keys('test@gmail.com')