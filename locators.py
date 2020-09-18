"""Simple registration form"""

from selenium import webdriver
import time

drive = webdriver.Chrome(r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe")
drive.get("http://suninjuly.github.io/simple_form_find_task.html")
print(drive.title)

# Filling registration form
drive.find_element_by_class_name("form-control").send_keys("Pierina Isabel")
drive.find_element_by_name("last_name").send_keys("Moreno Benavides")
drive.find_element_by_css_selector("[class='form-control city']").send_keys("Los Angeles")
drive.find_element_by_css_selector("[id='country']").send_keys("United State")

# Click on Submit bottom
drive.find_element_by_id("submit_button").click()

# Accepting Alert window
alert = drive.switch_to.alert
alert.accept()
time.sleep(5)
drive.quit()

