from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#driver.maximize_window()
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
time.sleep(3)
act_chian = ActionChains(driver)
elem = driver.find_element(By.XPATH,"//span[text()='right click me']")
act_chian.context_click(elem).perform()

right_click_menu = driver.find_elements(By.CSS_SELECTOR,'li.context-menu-item span')
for ele in right_click_menu:
    print(ele.text)
    if ele.text=='Edit':
        ele.click()
        break