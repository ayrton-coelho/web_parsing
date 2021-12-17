#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
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

driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[7]/td[2]/input[1]").send_keys("7")

driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[7]/td[2]/input[2]").send_keys("10")

driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[7]/td[2]/input[2]").send_keys("1")

driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[8]/td[2]/input[1]").send_keys("7")

driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[8]/td[2]/input[1]").send_keys("9")

driver.find_element(By.XPATH, "/html/body/form/p[1]/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[8]/td[2]/input[3]").send_keys("1")