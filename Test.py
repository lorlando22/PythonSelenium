from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import webelement
import time


from subprocess import check_output
check_output("C:\chromedriver_win32\RUNME.bat", shell=True)

time.sleep(5)


PATH = "C:\chromedriver_win32\chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")

driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

print(driver.title)

driver.close
driver.quit