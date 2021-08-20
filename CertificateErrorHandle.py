from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.chrome.options import  Options

# options = Options()
# options.add_argument('--allow-running-insecure-content')
# options.add_argument('--ignore-certificate-errors')

# desired_capabilities = DesiredCapabilities().CHROME.copy()
# desired_capabilities['acceptInsecureCerts'] = True


# options = Options()
# options.set_capability('acceptInsecureCerts',True)
# driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
# driver.implicitly_wait(10)


# driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=desired_capabilities)
# driver.implicitly_wait(10)

#


# Firfox

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=profile)

driver.get('https://expired.badssl.com/')

header_value = driver.find_element(By.TAG_NAME,'h1')
print(header_value.text)
