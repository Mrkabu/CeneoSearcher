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
driver.find_element(By.ID, Locators.fieldsearchceneo).send_keys(search, Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH, Locators.akceptuje).click()
time.sleep(3)

for elem in driver.find_elements_by_xpath('//a[@class="js_clickHash go-to-product"]'):
    p = elem.get_attribute('title')
    print(p)

search2 = input("Skopiuj z listy i wklej tutaj nazwę produktu który chcesz wyszukać, aby doprecyzować wyniki wyszukiwania: ")
driver.find_element_by_css_selector("[title^='" + search2 + "']").click()
time.sleep(3)

for element in driver.find_elements_by_xpath('//tr[@class="product-offer js_product-offer"]'):
    k = element.get_attribute('data-shopurl')
    t = element.get_attribute('data-price')
    log.write("Cena sprzętu [" + str(search2) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
    print(k, t)

for ele in driver.find_elements_by_xpath('//tr[@class="product-offer js_product-offer promoted"]'):
    q = ele.get_attribute('data-shopurl')
    z = ele.get_attribute('data-price')
    log.write("Cena sprzętu [" + str(search2) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
    print(q, z)