from selenium import webdriver
import time

PATH = r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe"
drive1 = webdriver.Chrome(executable_path=PATH)
validateText = "Option1"

drive1.get("https://rahulshettyacademy.com/AutomationPractice/")
drive1.find_element_by_css_selector('#name').send_keys(validateText)
drive1.find_element_by_id('alertbtn').click()
alertPopUp = drive1.switch_to.alert
alert = alertPopUp.text
assert validateText in alert
#alertPopUp.accept()
alertPopUp.dismiss()
