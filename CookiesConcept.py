from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#driver.maximize_window()
driver.get('https://www.reddit.com/')

cookies = driver.get_cookies()

print(len(cookies))
print(cookies)
driver.add_cookie({"name":"suhas",
                   "doman":"reddit.com",
                   "value":"python"})
print(len(cookies))
#