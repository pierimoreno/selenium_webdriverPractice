"""Technique Frames to handle with Selenium"""

from selenium import webdriver
import time

drive = webdriver.Chrome(r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe")
drive.get("https://the-internet.herokuapp.com/iframe")

#iFrame, frameset, frame
drive.switch_to.frame("mce_0_ifr")
drive.find_element_by_css_selector("#tinymce").clear()
drive.find_element_by_css_selector("#tinymce").send_keys("Automatization testing")
drive.switch_to.default_content()

print(drive.find_element_by_tag_name("h3").text)

