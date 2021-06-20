from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secret
from secret import pws
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://rpfs.rp.edu.sg/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2fmyleo.rp.edu.sg%2f&wreply=https%3a%2f%2fmyleo.rp.edu.sg%2fCoreBase%2fLogin%2fADFSAutoLogin%3fReturnUrl%3d%252FCoreBase%252FHome")
print(driver.title)

search = driver.find_element_by_name("UserName")
search.send_keys("21030228@rp.edu.sg")

search = driver.find_element_by_name("Password")
search.send_keys(pws)
search.send_keys(Keys.RETURN)
