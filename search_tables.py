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

for elem in driver.find_elements_by_xpath('//a[@class="js_clickHash go-to-product"]'):
    p = elem.get_attribute('title')
    table.append(p)

# r = len(table)

a = str(table[0])
b = str(table[1])
c = str(table[2])
d = str(table[3])
e = str(table[4])
f = str(table[5])

if search.casefold() in a.casefold():
    driver.find_element_by_css_selector("[title^='" + a + "']").click()
elif search.casefold() in b.casefold():
    driver.find_element_by_css_selector("[title^='" + b + "']").click()
elif search.casefold() in c.casefold():
    driver.find_element_by_css_selector("[title^='" + c + "']").click()
elif search.casefold() in d.casefold():
    driver.find_element_by_css_selector("[title^='" + d + "']").click()
elif search.casefold() in e.casefold():
    driver.find_element_by_css_selector("[title^='" + e + "']").click()
elif search.casefold() in f.casefold():
    driver.find_element_by_css_selector("[title^='" + f + "']").click()

time.sleep(2)

print("Oferty niepromowane:\n")
log.write("Oferty niepromowane:\n")

for element in driver.find_elements_by_xpath('//tr[@class="product-offer js_product-offer"]'):
    k = element.get_attribute('data-shopurl')
    t = element.get_attribute('data-price')
    log.write("Cena sprzętu [" + str(table[1]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
    print(k, t)

print("Oferty promowane:\n")
log.write("Oferty promowane:\n")

for ele in driver.find_elements_by_xpath('//tr[@class="product-offer js_product-offer promoted"]'):
    q = ele.get_attribute('data-shopurl')
    z = ele.get_attribute('data-price')
    log.write("Cena sprzętu [" + str(table[1]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
    print(q, z)