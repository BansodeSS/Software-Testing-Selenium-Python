import xlrd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.orangehrm.com/open-source/open-source-on-demand/')


url = driver.find_element(By.ID,'Form_submitForm_subdomain')
firstname = driver.find_element(By.ID,'Form_submitForm_FirstName')
lastname = driver.find_element(By.ID,'Form_submitForm_LastName')
company = driver.find_element(By.ID,'Form_submitForm_CompanyName')
email = driver.find_element(By.ID,'Form_submitForm_Email')
contact = driver.find_element(By.ID,'Form_submitForm_Contact')
country = driver.find_element(By.ID,'Form_submitForm_Country')


workbook = xlrd.open_workbook("example.xls")
sheet = workbook.sheet_by_name("registration")
rowCount = sheet.nrows
colCount = sheet.ncols
# print('How many rows are there',rowCount)
# print('How many columns are there',colCount)

for curr_row in range(1,rowCount):
    # user_name = sheet.cell_value(curr_row,0)
    # password = sheet.cell_value(curr_row, 1)
    urlvalue = sheet.cell_value(curr_row,0)
    firstnamevalue= sheet.cell_value(curr_row,1)
    lastnamevalue = sheet.cell_value(curr_row,2)
    companyvalue = sheet.cell_value(curr_row,3)
    emailvalue = sheet.cell_value(curr_row,4)
    contactvalue = sheet.cell_value(curr_row,5)
    countryvalue = sheet.cell_value(curr_row,6)

    url.send_keys(urlvalue)
    firstname.send_keys(firstnamevalue)
    lastname.send_keys(lastnamevalue)
    company.send_keys(companyvalue)
    email.send_keys(lastnamevalue)
    contact.send_keys(contactvalue)
    country.send_keys(countryvalue)
    time.sleep(3)
