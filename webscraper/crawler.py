import os
import time

from os import path
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

link_list = open("chefkochlinks.txt", "r").readlines().copy()
'''speichere Rezeptdaten für jedes Element in der Link-Liste'''

rezCounter = 0
rezMaximum = 10

"""falls bei rezept etwas schief geht """
corrupted = []

for link in link_list:

    if rezCounter > rezMaximum:
        break

    try:
        if len(link) == 0:
            continue
        '''Benutze die gedruckte Version wegen des Bildformates'''
        if not "chefkoch.de/rezepte/drucken" in str(link):
            link = str(link).replace("chefkoch.de/rezepte", "chefkoch.de/rezepte/drucken")

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
        if not os.path.exists(rezept_dir):
            os.mkdir(rezept_dir)
        else:
            """brich ab wenn Rezept schon vorhanden"""
            print("Rezept %s bereits vorhanden" % title)
            # continue

        """Vorschaubild: """
        time.sleep(2)

        # TODO: Bild in höherer Auflösung speichern (Originalbild bei Bild in neuem Tab anzeigen)
        '''Bild wird in projekt_dir gespeichert unter rezeptname.png '''
        driver.find_element(By.XPATH, "/html/body/main/div[3]/div[1]/div[1]/div/figure/amp-img/img").screenshot(
            rezept_dir + title + ".png")

        """speichere Kurzbeschreibung wenn vorhanden"""
        kurzbeschr = driver.find_element(By.XPATH, "/html/body/main/div[3]/div[2]/div[1]/h2").text
        if len(kurzbeschr) != 0:
            file = open(rezept_dir + "kurzbeschreibung.txt", "w")
            file.write(kurzbeschr)
            file.close()

        """Handlungsschritte müssen in Verarbeitung nur mit string.splitlines() zu einzelnen Elementen getrennt werden"""
        hschritte = driver.find_element(By.XPATH, "/html/body/main/div[3]/div[2]/div[2]/p").text
        """lösche leere Zeilen und speichere"""
        hschritte = os.linesep.join([s for s in hschritte.splitlines() if s])
        if len(hschritte) != 0:
            file = open(rezept_dir + "handlungsschritte.txt", "w")
            file.write(hschritte)
            file.close()

        """hole alle Zutaten mit Mengenangaben (Menge|Zutat)"""
        zutaten = []
        """im Seitenquelltext fangen Zutaten bei table row 2 an"""
        zutatRow = 2
        while True:
            """Manche Zutaten haben keine Mengenangabe"""
            try:
                menge = driver.find_element(By.XPATH,
                                            "/html/body/main/div[3]/div[1]/div[2]/table/tbody/tr[%d]/td[1]/span/strong" % zutatRow).text
            except:
                menge = ""

            """wenn zName nicht gefunden werden kann könnte es sich um Überschrift handeln -> suche 1 weiter unten"""
            try:
                zName = driver.find_element(By.XPATH,
                                            "/html/body/main/div[3]/div[1]/div[2]/table/tbody/tr[%d]/td[2]/span" % zutatRow).text
            except:
                """wenn das nur Überschrift ist wie 'für Belag', dann mach doch weiter """
                try:
                    zName = driver.find_element(By.XPATH,
                                                "/html/body/main/div[3]/div[1]/div[2]/table/tbody/tr[%d]/td[2]/span" % (zutatRow+1)).text
                    zutatRow += 1
                    continue
                except:
                    break

            """| als Trennzeichen"""
            menge = menge.replace("|", "/")
            zName = zName.replace("|", "/")
            zutaten.append(menge + "|" + zName)
            zutatRow += 1

        if len(zutaten) != 0:
            file = open(rezept_dir + "zutaten.txt", "w")
            """Zutaten untereinander in Liste schreiben"""
            file.write("\n".join(zutaten))
            file.close()



        main_link = link.replace("/drucken","")
        driver.get(main_link)


        """finde alle Tags"""
        tags = []
        while True:
            try:
                tag = driver.find_element(By.XPATH, "/html/body/main/article[4]/div[3]/amp-carousel/div/div[1]/div[%d]/a" % (len(tags)+1)).text
                tags.append(tag)
            except:
                break

        if tags.__len__() != 0:
            file = open(rezept_dir + "tags.txt", "w")
            """tags untereinander in Liste schreiben"""
            file.write("\n".join(tags))
            file.close()

        print(",".join(tags))

        rezCounter += 1

        print("%d finished %s" % (rezCounter, title))


    except:
        print("Fehler mit %s" % link)
        corrupted.append(link)
        file = open(projekt_dir + "corrupted.txt", "w")
        """corrupted untereinander in Liste schreiben"""
        file.write("\n".join(corrupted))
        file.close()


file = open(projekt_dir + "corrupted.txt", "w")
"""corrupted untereinander in Liste schreiben"""
file.write("\n".join(corrupted))
file.close()

driver.quit()


"""
Fehler im Scraper: bei neuer Überchrift wird aufgehört weiter Zutaten zu scrapen -> bsp 
https://www.chefkoch.de/rezepte/drucken/1219221227428135/Tomaten-Tarte-mit-Ziegenkaese.html


Überschrift NICHT MIT SCRAPEN! : 
/html/body/main/div[3]/div[1]/div[2]/table/tbody/tr[6]/td/span

Das hier mit scrapen
/html/body/main/div[3]/div[1]/div[2]/table/tbody/tr[4]/td[1]/span/strong
/html/body/main/div[3]/div[1]/div[2]/table/tbody/tr[7]/td[1]/span/strong

"""