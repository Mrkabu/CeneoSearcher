from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from ceneolocators import Locators
import datetime
import time

search = input("Podaj produkt do wyszukania: ")
log = open("C:/" + search + "_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".txt", "w+")
driver = webdriver.Chrome('D:\PycharmProjects\Drivery\chromedriver.exe')
driver.maximize_window()
driver.get(Locators.ceneo)
time.sleep(2)

driver.find_element(By.ID, Locators.fieldsearchceneo).send_keys(search, Keys.ENTER)
time.sleep(2)

driver.find_element(By.XPATH, Locators.akceptuje).click()
time.sleep(2)

table = []
table2 = []

for elem in driver.find_elements_by_xpath('//a[@class="js_clickHash go-to-product"]'):
    p = elem.get_attribute('title')
    table.append(p)

r = len(table)

for x in range(0, r):
    if search.casefold() in str(table[x]).casefold():
        a = str(table[x])
        table2.append(a)

if len(table2) == 0:
    print("Nie znaleziono wyszukiwanego sprzętu")
    log.write("Wpisano do wyszukania sprzęt [" + search + "]. Ceneo nie znalazło poprawnego rezultatu. Data wyszukania: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
else:
    driver.find_element_by_css_selector("[title^='" + str(table2[0]) + "']").click()
    time.sleep(2)
    print("\nOferty niepromowane:\n")
    log.write("Oferty niepromowane:\n")

    for element in driver.find_elements_by_xpath('//tr[@class="product-offer js_product-offer"]'):
        k = element.get_attribute('data-shopurl')
        t = element.get_attribute('data-price')
        log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
        print(k, t)

    print("\nOferty promowane:\n")
    log.write("\nOferty promowane:\n")

    for ele in driver.find_elements_by_xpath('//tr[@class="product-offer js_product-offer promoted"]'):
        q = ele.get_attribute('data-shopurl')
        z = ele.get_attribute('data-price')
        log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
        print(q, z)