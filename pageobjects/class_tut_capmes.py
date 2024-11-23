from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class capmes:

    fir_na = "//input[@id='input-firstname']"
    las_na = "//input[@id='input-lastname']"
    ne_pas = "//input[@id='input-password']"
    con_pas = "//input[@id='input-confirm']"
    con_but = "//input[@value='Continue']"
    em_il = "//input[@id='input-email']"



    def __init__(self,driver):
        self.driver = driver

    def first_name(self,fn):
        self.driver.find_element(By.XPATH,self.fir_na).send_keys(fn)

    def last_name(self,ln):
        self.driver.find_element(By.XPATH, self.las_na).send_keys(ln)

    @pytest.mark.dependency(name = 'send_email')
    def email(self,val):
        self.driver.find_element(By.XPATH,self.em_il).send_keys(val)
    @pytest.mark.dependency(depends = ['send_email'])
    def new_pass(self,np):
        self.driver.find_element(By.XPATH,self.ne_pas).send_keys(np)

    def confirm_pas(self,cnp):
        self.driver.find_element(By.XPATH,self.con_pas).send_keys(cnp)

    def confirm_but(self):
        self.driver.find_element(By.XPATH, self.con_but).click()
        time.sleep(5)
        wait = WebDriverWait(self.driver,10)
        w = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-danger alert-dismissible']")))
        me = w.text
        print(me)
        wait = WebDriverWait(self.driver, 10)
        we = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'E-Mail Address does not appear to be valid!')]")))
        exp = "E-Mail Address does not appear to be valid!"
        act = we.text
        print(act)
        time.sleep(5)
        self.driver.save_screenshot("screenshots/newsc.png")
        assert act == exp

