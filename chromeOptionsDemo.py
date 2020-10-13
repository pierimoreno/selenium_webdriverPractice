"""Chrome options"""


from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximixed")
chromeOptions.add_argument("headless")
chromeOptions.add_argument("--ignore-certificate-errors")

drive = webdriver.Chrome(r"C:\Users\pieri\PycharmProjects\appPython\Selenium\chromedriver.exe", options=chromeOptions)
drive.get("https://rahulshettyacademy.com/angularpractice/")

print(drive.title)