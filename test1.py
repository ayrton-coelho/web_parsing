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

time.sleep(6)

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

distancia_km = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[9]/td[2]/input")
distancia_km.send_keys("320")

""" Fecha salida """
driver.execute_script("document.getElementById('PEROCAFECSAL').setAttribute('value','20/12/2021')")

""" Hora salida """
driver.find_element(By.XPATH, "//*[@id='PEROCAHORSAL']/option[36]").click()

""" Fecha llegada"""
driver.execute_script("document.getElementById('PEROCAFECLLE').setAttribute('value','20/12/2021')")

""" Hora llegada (missing click) """
driver.find_element(By.XPATH, "//*[@id='PEROCAHORLLE']/option[6]")

registro = driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[15]/td[2]/input[1]")
registro.send_keys("200411")

""" Guardar """
driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
time.sleep(2)

""" Calles y rutas checkboxes """
driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[1]/div/table/tbody/tr[3]/td[3]/label/input").click()

""" Siguiente """
driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[3]/td/table/tbody/tr[2]/td/input[2]").click()
time.sleep(1)

""" Observaciones """
driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[1]/div/table/tbody/tr[1]/td[2]/label/input").click()
time.sleep(1)

""" Terminar """
driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[3]/td/table/tbody/tr[2]/td/input[3]").click()
