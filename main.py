from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#
# cursor = driver.find_element(By.ID, "buyCursor")
# cursor_txt = cursor.text
# cursor_list = cursor_txt.split()
# cursor_val = cursor_list[2].replace(",", "")
# cursor_val = int(cursor_val)
#
# grandma = driver.find_element(By.ID, "buyGrandma")
# grandma_txt = grandma.text
# grandma_list = grandma_txt.split()
# grandma_val = grandma_list[2].replace(",", "")
# grandma_val = int(grandma_val)
#
# factory = driver.find_element(By.ID, "buyFactory")
# factory_txt = factory.text
# factory_list = factory_txt.split()
# factory_val = factory_list[2].replace(",", "")
# factory_val = int(factory_val)
#
# mine = driver.find_element(By.ID, "buyMine")
# mine_txt = mine.text
# mine_list = mine_txt.split()
# mine_val = mine_list[2].replace(",", "")
# mine_val = int(mine_val)
#
# shipment = driver.find_element(By.ID, "buyShipment")
# shipment_txt = shipment.text
# shipment_list = shipment_txt.split()
# shipment_val = shipment_list[2].replace(",", "")
# shipment_val = int(shipment_val)
#
# alchemy = driver.find_element(By.ID, "buyAlchemy lab")
# alchemy_txt = alchemy.text
# alchemy_list = alchemy_txt.split()
# alchemy_val = alchemy_list[3].replace(",", "")
# alchemy_val = int(alchemy_val)
#
# portal = driver.find_element(By.ID, "buyPortal")
# portal_txt = portal.text
# portal_list = portal_txt.split()
# portal_val = portal_list[2].replace(",", "")
# portal_val = int(portal_val)
#
# time_machine = driver.find_element(By.ID, "buyTime machine")
# time_machine_txt = time_machine.text
# time_machine_list = time_machine_txt.split()
# time_machine_val = time_machine_list[3].replace(",", "")
# time_machine_val = int(time_machine_val)


def point_check():
    cursor = driver.find_element(By.ID, "buyCursor")
    cursor_txt = cursor.text
    cursor_list = cursor_txt.split()
    cursor_val = cursor_list[2].replace(",", "")
    cursor_val = int(cursor_val)

    grandma = driver.find_element(By.ID, "buyGrandma")
    grandma_txt = grandma.text
    grandma_list = grandma_txt.split()
    grandma_val = grandma_list[2].replace(",", "")
    grandma_val = int(grandma_val)

    factory = driver.find_element(By.ID, "buyFactory")
    factory_txt = factory.text
    factory_list = factory_txt.split()
    factory_val = factory_list[2].replace(",", "")
    factory_val = int(factory_val)

    mine = driver.find_element(By.ID, "buyMine")
    mine_txt = mine.text
    mine_list = mine_txt.split()
    mine_val = mine_list[2].replace(",", "")
    mine_val = int(mine_val)

    shipment = driver.find_element(By.ID, "buyShipment")
    shipment_txt = shipment.text
    shipment_list = shipment_txt.split()
    shipment_val = shipment_list[2].replace(",", "")
    shipment_val = int(shipment_val)

    alchemy = driver.find_element(By.ID, "buyAlchemy lab")
    alchemy_txt = alchemy.text
    alchemy_list = alchemy_txt.split()
    alchemy_val = alchemy_list[3].replace(",", "")
    alchemy_val = int(alchemy_val)

    portal = driver.find_element(By.ID, "buyPortal")
    portal_txt = portal.text
    portal_list = portal_txt.split()
    portal_val = portal_list[2].replace(",", "")
    portal_val = int(portal_val)

    time_machine = driver.find_element(By.ID, "buyTime machine")
    time_machine_txt = time_machine.text
    time_machine_list = time_machine_txt.split()
    time_machine_val = time_machine_list[3].replace(",", "")
    time_machine_val = int(time_machine_val)

    check = driver.find_element(By.XPATH, '//*[@id="money"]')
    money = int(check.text)
    if money > time_machine_val:
        time_machine = driver.find_element(By.ID, "buyTime machine")
        time_machine.click()
    elif money > portal_val:
        portal = driver.find_element(By.ID, "buyPortal")
        portal.click()
    elif money > alchemy_val:
        alchemy = driver.find_element(By.ID, "buyAlchemy lab")
        alchemy.click()
    elif money > shipment_val:
        shipment = driver.find_element(By.ID, "buyShipment")
        shipment.click()
    elif money > mine_val:
        mine = driver.find_element(By.ID, "buyMine")
        mine.click()
    elif money > factory_val:
        factory = driver.find_element(By.ID, "buyFactory")
        factory.click()
    elif money > grandma_val:
        grandma = driver.find_element(By.ID, "buyGrandma")
        grandma.click()
    else:
        cursor = driver.find_element(By.ID, "buyCursor")
        cursor.click()


click_per_sec = driver.find_element(By.XPATH, '//*[@id="cps"]')

timeout = time.time() + 60*5
check_sec = time.time() + 5

game_on = True

while game_on:
    time_start = time.time()
    if time_start > check_sec:
        check_sec = time_start + 5
        point_check()

    if time_start < timeout:
        cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
        cookie.click()
        cookie.click()

    else:
        game_on = False
        print(click_per_sec.text)
        driver.quit()









