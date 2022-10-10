import os
import time

from os import path, replace
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.headless = False
options.add_argument("--window-size=1800,900")
'''Cookies werden automatisch akzeptiert'''
options.add_extension('i-don-t-care-about-cookies.crx')

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

projekt_dir = path.dirname(path.realpath(__file__)) + "\\"

links = ["https://www.chefkoch.de/rezepte/2712951424287361/Spinatstrudel-mit-getrockneten-Tomaten-und-Walnuessen.html"]

driver.get(links[0])

maxLinks = 1000

"""Tiefensuche nach neuen Rezeptlinks:"""
def getLinks(_links):

    if len(links) > maxLinks:
        file = open(projekt_dir + "chefkochlinks2.txt", "w")
        """links untereinander in Liste schreiben"""
        file.write("\n".join(links))
        file.close()

        driver.quit()
        exit(0)


    for link in _links:
        if link in links or "https://www.chefkoch.de/rezepte/" not in link:
            continue

        driver.get(link)
        links.append(link)

        if len(links) > maxLinks:
            file = open(projekt_dir + "chefkochlinks2.txt", "w")
            """links untereinander in Liste schreiben"""
            file.write("\n".join(links))
            file.close()

            driver.quit()
            exit(0)

        if len(links) % 50 == 0:
            file = open(projekt_dir + "chefkochlinks2.txt", "w")
            """links untereinander in Liste schreiben"""
            file.write("\n".join(links))
            file.close()

        print("appended %d %s " % (len(links), link))

        new_links = []
        for i in range(5):

            try:
                ref = driver.find_element(By.XPATH, "/html/body/main/aside[1]/div/amp-carousel/div/div[1]/a[%d]" % (i+1)).get_attribute("href")
                new_links.append(ref)
            except:
                print("kein weiteres elem von 5 gefunden")
                break

        for i in range(3):
            try:
                ref = driver.find_element(By.XPATH, "/html/body/main/aside[3]/div/a[%d]" % (i+1)).get_attribute("href")
                new_links.append(ref)
            except:
                print("kein weiteres elem von 3 gefunden")
                break

        getLinks(new_links)


new_links = []
for i in range(5):
    try:
        ref = driver.find_element(By.XPATH,
                                  "/html/body/main/aside[1]/div/amp-carousel/div/div[1]/a[%d]" % (i + 1)).get_attribute(
            "href")
        new_links.append(ref)
    except:
        print("kein weiteres elem von 5 gefunden")
        break

    getLinks(new_links)


file = open(projekt_dir + "chefkochlinks2.txt", "w")
"""Zutaten untereinander in Liste schreiben"""
file.write("\n".join(links))
file.close()

driver.quit()