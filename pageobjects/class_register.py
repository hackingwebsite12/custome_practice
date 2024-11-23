import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class register_page:

    username =  "// input[ @ id = 'input-username']"
    firstname = "//input[@id='input-firstname']"
    lastname = "//input[@id='input-lastname']"
    email = "//input[@id='input-email']"
    country = "//select[@id='input-country']"
    password = "//input[@id='input-password']"
    register_button = "//button[@class='btn btn-primary btn-lg hidden-xs']"
    moveregister = "//a[@class='btn btn-black navbar-btn']"

    def __init__(self,driver):
        self.driver = driver

    def user_name(self,usrname):
        wait = WebDriverWait(self.driver,30)
        we = wait.until(EC.visibility_of_element_located((By.XPATH,self.username))).send_keys(usrname)


    def first_name(self,frstname):
        self.driver.find_element(By.XPATH,self.firstname).send_keys(frstname)

    def last_name(self,lstname):
        self.driver.find_element(By.XPATH,self.lastname).send_keys(lstname)

    def e_mail(self,mail):
        self.driver.find_element(By.XPATH,self.email).send_keys(mail)

    def countries(self):
        we = self.driver.find_element(By.XPATH,self.country)
        sel = Select(we)
        sel.select_by_visible_text("India")

    def pass_word(self,pword):
        self.driver.find_element(By.XPATH,self.password).send_keys(pword)

    def reg_but(self):
        self.driver.find_element(By.XPATH,self.register_button).click()

    def move_register_page(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.moveregister).click()

