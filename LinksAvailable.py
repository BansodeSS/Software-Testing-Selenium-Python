from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.get('https://www.amazon.in')
# linksList = driver.find_elements(By.TAG_NAME,'a')
# print(len(linksList))
#
# for ele in linksList:
#     link_text = ele.text
#     print(link_text)
#     print(ele.get_attribute('href'))
#
imagesList = driver.find_elements(By.TAG_NAME,'img')
print(len(imagesList))

for img in imagesList:

    print(img.get_attribute('src'))