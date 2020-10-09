"""Interections with Browser using actions"""

from selenium import webdriver
from selenium.webdriver import ActionChains


drive = webdriver.Chrome(r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe")
drive.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(drive)
menu = drive.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
childMenu = drive.find_element_by_link_text("Top")
action.move_to_element(childMenu).click().perform()
