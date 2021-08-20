from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#driver.maximize_window()
driver.get('http://www.londonfreelance.org/courses/frames/index.html')
#driver.switch_to.frame(2)
#driver.switch_to.frame('main')
frame_element = driver.find_element(By.NAME,'main')
driver.switch_to.frame(frame_element)
heade_value = driver.find_element(By.CSS_SELECTOR,"body > h2").text
print(heade_value)
