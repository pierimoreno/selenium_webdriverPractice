"""  Completed Checkout task """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


from selenium.webdriver.support.select import Select
import time

drive = webdriver.Chrome(r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe")
drive.get("https://rahulshettyacademy.com/angularpractice/shop")

products = drive.find_elements_by_xpath("//div[@class='card h-100']")
# //div/h4/a
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_css_selector('[class="btn btn-info"]').click()

drive.find_element_by_css_selector("a.btn-primary").click()

checkoutItem = drive.find_element_by_xpath("//div/h4/a").text
print(checkoutItem)
assert "Blackberry" == checkoutItem, "Not Blackberry phone have been found"

drive.find_element_by_css_selector('[class="btn btn-success"]').click()
drive.find_element_by_xpath("//input[@id='country']").send_keys("ind")

wait = WebDriverWait(drive, 7)
wait.until(expected_conditions.presence_of_element_located((By. LINK_TEXT, "India")))
drive.find_element_by_xpath("//a[text()='India']").click()
drive.find_element_by_css_selector('[class="checkbox checkbox-primary"]').click()
drive.find_element_by_class_name("btn-lg").click()

successText = drive.find_element_by_css_selector("div.alert-success").text
assert "Success!" in successText

drive.get_screenshot_as_file("screen.png")







