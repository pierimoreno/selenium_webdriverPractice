'''A simple example to how handle a Child Window '''

from selenium import webdriver
import time

drive = webdriver.Chrome(r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe")
drive.get("https://the-internet.herokuapp.com/windows")

drive.find_element_by_link_text("Click Here").click()
print(drive.find_element_by_xpath("//div/h3").text)

newWindow = drive.window_handles[1]
drive.switch_to.window(newWindow)
print(drive.find_element_by_xpath("//div/h3").text)