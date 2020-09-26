import drive as drive
from selenium import webdriver
import time
PATH = r"C:\Users\pieri\PycharmProjects\appPython\Selenium\geckodriver.exe"
from selenium.webdriver.support.select import Select

# drive = webdriver.Chrome(r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe")
drive = webdriver.Firefox(executable_path=PATH)

drive.get('https://www.rahulshettyacademy.com/AutomationPractice/')

drive.find_element_by_css_selector('[id="autocomplete"]').send_keys('California')

dropdwon_gender = Select(drive.find_element_by_id("dropdown-class-example"))
dropdwon_gender.select_by_value("option3")

message1 = drive.find_element_by_css_selector('div[class="cen-left-align"] legend:nth-child(1)').text
assert "Suggession" in message1

message2 = drive.find_element_by_css_selector('div[class="cen-right-align"] legend:nth-child(1)').text
assert "Dropdown Example" == message2
