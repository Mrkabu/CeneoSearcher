from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from ceneolocators import Locators
import datetime
import time

search = input('Podaj produkt do wyszukania: ')

num = input('Podaj liczbę sklepów (od 1 do 10, 0 dla wyszukania we wszystkich sklepach): ')
opi = 1

if num == '0':
    print('Wyszukiwanie we wszystkich sklepach')
    shop1 = 0
    shop2 = 0
    shop3 = 0
    shop4 = 0
    shop5 = 0
    shop6 = 0
    shop7 = 0
    shop8 = 0
    shop9 = 0
    shop10 = 0
elif num == '1':
    shop1 = input('Nazwa 1 sklepu: ')
elif num == '2':
    shop1 = input('Nazwa 1 sklepu: ')
    shop2 = input('Nazwa 2 sklepu: ')
elif num == '3':
    shop1 = input('Nazwa 1 sklepu: ')
    shop2 = input('Nazwa 2 sklepu: ')
    shop3 = input('Nazwa 3 sklepu: ')
elif num == '4':
    shop1 = input('Nazwa 1 sklepu: ')
    shop2 = input('Nazwa 2 sklepu: ')
    shop3 = input('Nazwa 3 sklepu: ')
    shop4 = input('Nazwa 4 sklepu: ')
elif num == '5':
    shop1 = input('Nazwa 1 sklepu: ')
    shop2 = input('Nazwa 2 sklepu: ')
    shop3 = input('Nazwa 3 sklepu: ')
    shop4 = input('Nazwa 4 sklepu: ')
    shop5 = input('Nazwa 5 sklepu: ')
elif num == '6':
    shop1 = input('Nazwa 1 sklepu: ')
    shop2 = input('Nazwa 2 sklepu: ')
    shop3 = input('Nazwa 3 sklepu: ')
    shop4 = input('Nazwa 4 sklepu: ')
    shop5 = input('Nazwa 5 sklepu: ')
    shop6 = input('Nazwa 6 sklepu: ')
elif num == '7':
    shop1 = input('Nazwa 1 sklepu: ')
    shop2 = input('Nazwa 2 sklepu: ')
    shop3 = input('Nazwa 3 sklepu: ')
    shop4 = input('Nazwa 4 sklepu: ')
    shop5 = input('Nazwa 5 sklepu: ')
    shop6 = input('Nazwa 6 sklepu: ')
    shop7 = input('Nazwa 7 sklepu: ')
elif num == '8':
    shop1 = input('Nazwa 1 sklepu: ')
    shop2 = input('Nazwa 2 sklepu: ')
    shop3 = input('Nazwa 3 sklepu: ')
    shop4 = input('Nazwa 4 sklepu: ')
    shop5 = input('Nazwa 5 sklepu: ')
    shop6 = input('Nazwa 6 sklepu: ')
    shop7 = input('Nazwa 7 sklepu: ')
    shop8 = input('Nazwa 8 sklepu: ')
elif num == '9':
    shop1 = input('Nazwa 1 sklepu: ')
    shop2 = input('Nazwa 2 sklepu: ')
    shop3 = input('Nazwa 3 sklepu: ')
    shop4 = input('Nazwa 4 sklepu: ')
    shop5 = input('Nazwa 5 sklepu: ')
    shop6 = input('Nazwa 6 sklepu: ')
    shop7 = input('Nazwa 7 sklepu: ')
    shop8 = input('Nazwa 8 sklepu: ')
    shop9 = input('Nazwa 9 sklepu: ')
elif num == '10':
    shop1 = input('Nazwa 1 sklepu: ')
    shop2 = input('Nazwa 2 sklepu: ')
    shop3 = input('Nazwa 3 sklepu: ')
    shop4 = input('Nazwa 4 sklepu: ')
    shop5 = input('Nazwa 5 sklepu: ')
    shop6 = input('Nazwa 6 sklepu: ')
    shop7 = input('Nazwa 7 sklepu: ')
    shop8 = input('Nazwa 8 sklepu: ')
    shop9 = input('Nazwa 9 sklepu: ')
    shop10 = input('Nazwa 10 sklepu: ')
else:
    print('Podałeś nieprawidłową licbę sklepów!')
    raise SystemExit

log = open('C:/' + search + '_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.txt', 'w+')

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

        if str(shop1[0:2]).casefold() in str(k[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)
        elif str(shop2[0:2]).casefold() in str(k[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)
        elif str(shop3[0:2]).casefold() in str(k[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)
        elif str(shop4[0:2]).casefold() in str(k[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)
        elif str(shop5[0:2]).casefold() in str(k[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)
        elif str(shop6[0:2]).casefold() in str(k[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)
        elif str(shop7[0:2]).casefold() in str(k[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)
        elif str(shop8[0:2]).casefold() in str(k[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)
        elif str(shop9[0:2]).casefold() in str(k[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)
        elif str(shop10[0:2]).casefold() in str(k[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)
        elif num == '0':
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(k) + " wynosi " + str(t) + " zł" + "\n")
            print(k, t)


    print("\nOferty promowane:\n")
    log.write("\nOferty promowane:\n")

    for ele in driver.find_elements_by_xpath('//tr[@class="product-offer js_product-offer promoted"]'):
        q = ele.get_attribute('data-shopurl')
        z = ele.get_attribute('data-price')

        if str(shop1[0:2]).casefold() in str(q[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)
        elif str(shop2[0:2]).casefold() in str(q[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)
        elif str(shop3[0:2]).casefold() in str(q[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)
        elif str(shop4[0:2]).casefold() in str(q[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)
        elif str(shop5[0:2]).casefold() in str(q[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)
        elif str(shop6[0:2]).casefold() in str(q[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)
        elif str(shop7[0:2]).casefold() in str(q[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)
        elif str(shop8[0:2]).casefold() in str(q[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)
        elif str(shop9[0:2]).casefold() in str(q[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)
        elif str(shop10[0:2]).casefold() in str(q[0:2]).casefold():
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)
        elif num == '0':
            log.write("Cena sprzętu [" + str(table2[0]) + "] w dniu " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " w sklepie " + str(q) + " wynosi " + str(z) + " zł" + "\n")
            print(q, z)