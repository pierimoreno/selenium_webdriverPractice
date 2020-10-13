"""JavaScript executor"""
#Js DOM can acces any element on web pages just like how Selenium does
# Selenium have method javascript code in it

from selenium import webdriver


drive = webdriver.Chrome(r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe")
drive.get("https://rahulshettyacademy.com/angularpractice/")
drive.find_element_by_name("name").send_keys("Hello there")
print(drive.find_element_by_name("name").get_attribute("value"))
print(drive.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = drive.find_element_by_xpath("//a[text()='Shop']")
drive.execute_script("arguments[0].click();", shopButton)
drive.execute_script("window.scrollTo(0,document.body.scrollHeight);")
