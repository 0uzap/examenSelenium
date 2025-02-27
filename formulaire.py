import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()

driver.get("https://www.bricodepot.fr/")

driver.implicitly_wait(10)
driver.maximize_window()

actions  = ActionChains(driver)

btn_cookie = driver.find_element(By.ID, "didomi-notice-agree-button")
btn_cookie.click()
time.sleep(2) 

btn_co = driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div[2]/div/nav/div[2]')
btn_co.click()
time.sleep(2)

btn_compte = driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div[2]/div/nav/div[2]/div[2]/div[2]/div[1]/div/button')
btn_compte.click()
time.sleep(2)

genre = driver.find_element(By.ID, "bd-AccountCreation-civilite-homme")
genre.click()
prenom = driver.find_element(By.ID, "bd-AccountCreation-firstname")
prenom.send_keys("Pierre")
nom = driver.find_element(By.ID, "bd-AccountCreation-lastname")
nom.send_keys("Afeu")
# dropdown = Select(driver.find_element(By.ID, "bd-AccountCreation-select jsbd-AccountCreation-dropdown-select"))
# dropdown.select_by_visible_text("08 - CHARLEVILLE")
cp = driver.find_element(By.ID, "bd-AccountCreation-postalCode")
cp.send_keys("59000")
ville = driver.find_element(By.ID, "bd-AccountCreation-city")
ville.send_keys("TrucVille")
adresse = driver.find_element(By.ID, "bd-AccountCreation-address")
adresse.send_keys("32 rue de machin")
telephone = driver.find_element(By.ID, "bd-AccountCreation-phoneNumber")
telephone.send_keys("0123456789")
email = driver.find_element(By.ID, "bd-AccountCreation-email")
email.send_keys("afeupierre@gmail.com")
mdp = driver.find_element(By.ID, "bd-accountCreation-password")
mdp.send_keys("M0t2p@ss3")
envoyer = driver.find_element(By.XPATH, '//*[@id="accountInfo"]/div[6]/div[2]/button')
driver.execute_script("arguments[0].scrollIntoView();", envoyer)

time.sleep(2)

envoyer.click()

time.sleep(2)