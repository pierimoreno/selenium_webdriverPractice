from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time



# Implicit wait
# Explicit wait-

PATH = r"C:\Users\pieri\PycharmProjects\appPython\Selenium\geckodriver.exe"
drive1 = webdriver.Firefox(executable_path=PATH)

drive1.get("https://rahulshettyacademy.com/seleniumPractise/#/")
drive1.find_element_by_css_selector('[class="search-keyword"]').send_keys('ber')

drive1.find_element_by_class_name("search-button").click()
time.sleep(4)
count = len(drive1.find_elements_by_xpath("//div[@class='product']"))
assert count == 3

carButton = drive1.find_elements_by_xpath("//div[@class='product-action']/button")
for buttons in carButton:
    buttons.click()

drive1.find_element_by_css_selector('[alt="Cart"]').click()
drive1.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(drive1, 5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

drive1.find_element_by_class_name("promoCode").send_keys('rahulshettyacademy')
drive1.find_element_by_css_selector('[class="promoBtn"]').click()

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoCode')))
print(drive1.find_element_by_class_name('promoCode').text)

