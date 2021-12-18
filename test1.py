#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

PATH = "../chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://autogestion.dnt.gub.uy/saev31/hsignin.aspx")

userId = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[11]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/input")
userId.send_keys("07066810")

passwd = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[11]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input")
passwd.send_keys("gust1664")

time.sleep(5)

driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[11]/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td/table/tbody/tr/td/input").click()

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[1]/div/div/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[6]/tbody/tr[2]/td").click()

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[3]/td/table/tbody/tr[1]/td/input[1]").click()

time.sleep(5)

origen_1 = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[7]/td[2]/input[1]")
origen_1.send_keys("7")

origen_2 = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[7]/td[2]/input[2]")
origen_2.send_keys("10")

origen_3 = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[7]/td[2]/input[3]")
origen_3.send_keys("1")

destino_1 = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[8]/td[2]/input[1]")
destino_1.send_keys("7")

destino_2 = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[8]/td[2]/input[2]")
destino_2.send_keys("9")

destino_3 = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[8]/td[2]/input[3]")
destino_3.send_keys("1")

km = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[9]/td[2]/input")
km.send_keys("320")

driver.execute_script("document.getElementById('PEROCAFECSAL').setAttribute('value','10/01/2022')")

select = driver.find_element(By.XPATH, "//*[@id='PEROCAHORSAL']/option[2]").click()