import drive as drive
from selenium import webdriver
import time

PATH = r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe"
drive1 = webdriver.Chrome(executable_path=PATH)

drive1.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
checkboxes = drive1.find_elements_by_xpath('//input[@type="checkbox"]')
print(len(checkboxes))

for selection in checkboxes:
    selection.click()
    assert selection.is_selected()




