from selenium import webdriver
import time

# Implicit wait
# Explicit wait

PATH = r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe"
drive1 = webdriver.Chrome(executable_path=PATH)

drive1.implicitly_wait(5)
# wait until 5 seconds if objets is not displayed
# 1.5 seconds to reach next page-execution will resume in 1.5 seconds
# if object do not show at all, when max tike the test waits for 5 seconds

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

drive1.find_element_by_class_name("promoCode").send_keys('rahulshettyacademy')
drive1.find_element_by_css_selector('[class="promoBtn"]').click()
print(drive1.find_element_by_css_selector('[class="promoInfo"]').text)
