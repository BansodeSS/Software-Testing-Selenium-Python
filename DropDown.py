from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

def select_values(element,values):
    select = Select(element)
    select.select_by_visible_text(values)

def select_values_from_dropdown(dropDownOptionList,value):

    for ele in dropDownOptionList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

#ele_indust = driver.find_element(By.ID,'Form_submitForm_Industry')
#ele_contry = driver.find_element(By.ID,'Form_submitForm_Country')
#select_values(ele_indust,'Education')
#select_values(ele_contry,'India')

#select = Select(ele_indust)
#index_list = select.options

#for ele in index_list:
 #   print(ele.text)
 #   if (ele.text=='Automotive'):
  #      ele.click()
   #     break

indud_options = driver.find_elements(By.XPATH,'//select[@id="Form_submitForm_Industry"]/option')
print(len(indud_options))
select_values_from_dropdown(indud_options,'Education')