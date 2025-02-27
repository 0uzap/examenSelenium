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

btn_cookie = driver.find_element(By.XPATH, '//*[@id="didomi-notice-disagree-button"]')
btn_cookie.click()
time.sleep(2) 


btn_arrive = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/div[2]/div[1]/a[1]')
btn_arrive.click()
time.sleep(2)

arrivage = driver.find_elements(By.CLASS_NAME, "bd-ProductsListItem-link")
print(f"Il y a actuellement {len(arrivage)} articles en arrivage")

# titreArticle = driver.find_elements(By, "bd-ProductsListItem-title")
# prixArticle = driver.find_elements(By, "bd-Price bd-Price-no-operation")

for i in arrivage:
    titreArticle = i.find_element(By.CLASS_NAME, "bd-ProductsListItem-title").text
    prixArticle = i.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[4]/div/div[1]/div[2]/div/div/div[3]/a/div/div[3]/div[2]/div/div[2]").text
    print(f"Cet article: " + titreArticle + " coûte: " + prixArticle)
   