from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import webelement
import time

PATH = "C:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")

element = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
element.send_keys("Nicolas Papaccio")
time.sleep(3)

element = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
element.click()
time.sleep(5)

element = driver.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[4]/div/div/div[1]/a/h3")
element.click()
time.sleep(5)

element = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/span/h1")
facebookName = element.text

print(facebookName)

print("hello world")

driver.close
driver.quit