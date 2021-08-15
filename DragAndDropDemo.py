from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#driver.maximize_window()
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
time.sleep(3)

sorce_elem = driver.find_element(By.ID,'draggable')
target_elem = driver.find_element(By.ID,'droppable')

act_chains = ActionChains(driver)
#act_chains.drag_and_drop(sorce_elem,target_elem).perform()
act_chains.click_and_hold(sorce_elem).move_to_element(target_elem).release().perform()