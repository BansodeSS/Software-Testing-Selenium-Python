from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.spicejet.com')
time.sleep(3)

login_element = driver.find_element(By.ID,'ctl00_HyperLinkLogin')
act_chain = ActionChains(driver)
act_chain.move_to_element(login_element).perform()

spice_club_member_ele=driver.find_element(By.LINK_TEXT,'SpiceClub Members')
act_chain.move_to_element(spice_club_member_ele).perform()

member_login_element = driver.find_element(By.LINK_TEXT,'Member Login')
member_login_element.click()
time.sleep(3)
driver.quit()