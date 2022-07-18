import os
import time

from os import path, replace
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import shutil

options = Options()
options.headless = False
options.add_argument("--window-size=1800,900")
'''Cookies werden automatisch akzeptiert'''
options.add_extension('i-don-t-care-about-cookies.crx')

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

projekt_dir = path.dirname(path.realpath(__file__)) + "\\"

link_list = open("corrupted.txt", "r").readlines()


for link in link_list:

    if len(link) == 0:
        continue
    link = link.replace("\n", "")

    '''website not found vorbeugen'''
    time.sleep(1)

    try:
        driver.get(str(link))
    except:
        print("Link %s nicht gefunden" % link)
        continue

    title = str(driver.find_element(By.XPATH, value='/html/body/main/div[3]/div[2]/div[1]/h1/a').text)

    '''neues Directory für Rezept erstellen'''
    rezept_dir = path.dirname(path.realpath(__file__)) + "\\Rezepte\\%s\\" % title
    if os.path.exists(rezept_dir):
        shutil.rmtree(rezept_dir)


driver.quit()