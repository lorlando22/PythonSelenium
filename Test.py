from selenium import webdriver
PATH = "C:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.infobae.com")
print(driver.title)