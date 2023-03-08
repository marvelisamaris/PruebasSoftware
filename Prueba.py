# Marvelis Amaris Navarro CC. 1127661545
# Caterine sarmiento  cc: 1216721025


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/register.php")

name = driver.find_element(By.NAME, 'firstName')
name.send_keys("Marvelis" + Keys.TAB)

apellido = driver.find_element(By.NAME, 'lastName')
apellido.send_keys("Amaris" + Keys.TAB)

email = driver.find_element(By.NAME, 'email')
email.send_keys("amaris13@gmail.com" + Keys.TAB)

contraseña = driver.find_element(By.NAME, "password")
contraseña.send_keys("Contraseña123." + Keys.TAB)

conf_contra = driver.find_element(By.NAME, "confirmPassword")
conf_contra.send_keys("Contraseña123." + Keys.ENTER)

time.sleep(10)
