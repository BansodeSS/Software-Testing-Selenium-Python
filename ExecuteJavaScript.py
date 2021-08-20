from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

# driver.get('https://www.amazon.in')
# best_seller = driver.find_element(By.LINK_TEXT,'Best Sellers')
# # driver.execute_script("arguments[0].click();",best_seller)
#
# # inner_txt = driver.execute_script("return document.documentElement.innerText")
# # print(inner_txt)
#
# #driver.execute_script("arguments[0].style.border ='3px solid red' ",best_seller)
#
# # do the complete scroll down
#
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

driver.get('https://classic.crmpro.com/index.html')
forgot_pwd  = driver.find_element(By.LINK_TEXT,'Forgot Password?')
# driver.execute_script("arguments[0].click();",best_seller)

# inner_txt = driver.execute_script("return document.documentElement.innerText")
# print(inner_txt)

#driver.execute_script("arguments[0].style.border ='3px solid red' ",best_seller)

# do the complete scroll down

driver.execute_script("arguments[0].scrollIntoView(true);",forgot_pwd)