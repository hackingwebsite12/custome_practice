import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def test_variety():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    ele = driver.find_element(By.XPATH ,"//input[@id='twotabsearchtextbox']")
    act = ActionChains(driver)
    act.move_to_element(ele).click().send_keys("samsung s24 ultra 5g mobile").send_keys(Keys.ENTER).perform()
    time.sleep(3)

    li = driver.find_elements(By.XPATH ,"//div//span[contains(text(),'Samsung Galaxy S24 Ultra 5G')]")
    time.sleep(3)

    for i in li:
        if 'Titanium Black' in i.text:
            i.click()
            time.sleep(3)

#s = input("please click enter:")