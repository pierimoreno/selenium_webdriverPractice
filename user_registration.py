"""New user registration at Pluto.tv"""

from selenium import webdriver
import time

drive = webdriver.Chrome(r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe")
drive.get("https://pluto.tv/live-tv/threes-company")
time.sleep(8)

#click on emerges windows
drive.find_element_by_css_selector('[class="MuiButtonBase-root MuiButton-root jss9 MuiButton-text jss10 MuiButton-textSizeLarge MuiButton-sizeLarge"]>[class="MuiButton-label jss8"]').click()
drive.find_element_by_css_selector('[class="MuiSvgIcon-root jss71 jss72"]').click()

drive.find_element_by_class_name("jss23.jss24").click()
time.sleep(2)
drive.find_element_by_class_name("MuiButton-label").click()


#Filling sign up registration

drive.find_element_by_css_selector('[name="firstName"]').send_keys("Pierina")

#insert email
gmail = drive.find_element_by_name("email").click()
time.sleep(1)
drive.find_element_by_name("email").send_keys("pierinamoreno94@gmail.com")

#insert password
password = drive.find_element_by_name("password").click()
time.sleep(1)
drive.find_element_by_name("password").send_keys("television18.")

#year selection
drive.find_element_by_css_selector('[class="MuiSelect-root-171 MuiSelect-select-172 MuiSelect-selectMenu-175 MuiInputBase-input-163 MuiInput-input-151"]').click()
drive.find_element_by_css_selector('[data-value="Fri, 01 Jan 1993 08:00:00 GMT"]').click() #selection of the year

#sign up
drive.find_element_by_css_selector('[class="MuiButton-label-188 jss186"]').click()








