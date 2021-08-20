from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.headless =False
options.add_argument('--incognito')

#headless make it true
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(10)
#driver.maximize_window()
# options = webdriver.FirefoxOptions()
# options.headless = True
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)

driver.get('https://www.reddit.com/')
print(driver.title)