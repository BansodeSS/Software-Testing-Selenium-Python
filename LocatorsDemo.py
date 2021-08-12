from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)

username_url = driver.find_element(By.ID,'Form_submitForm_subdomain')
first_Name = driver.find_element(By.ID,'Form_submitForm_Name')
#last_Name = driver.find_element(By.ID,'Form_submitForm_LastName')
#job_Title = driver.find_element(By.ID,'Form_submitForm_subdomain')
#email = driver.find_element(By.ID,'Form_submitForm_subdomain')
#company = driver.find_element(By.ID,'Form_submitForm_subdomain')
total_link = driver.find_elements(By.TAG_NAME,'a')
image_list = driver.find_elements(By.TAG_NAME,'img')
username_url.send_keys("TestingDemo")
first_Name.send_keys("TestingDemo")
#last_Name.send_keys("TestingDemo")

#feature_link = driver.find_element(By.CLASS_NAME,'trial-btn').click()
#for ele in total_link:
   # print(ele.text)
    #print(ele.get_attribute('href'))
#
# for ele in image_list:
#     print(ele.get_attribute('src'))
# print(len(total_link))
#driver.quit()