from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class admin_entering:

    admin_red = "//a[@href='https://demo.opencart.com/admin/']"
    login_username = "//input[@id='input-username']"
    login_password = "//input[@id='input-password']"
    login_click_button = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def admin_opening(self):
        self.driver.find_element(By.XPATH,self.admin_red).click()

    #def l_username(self,dem):
     #   self.driver.implicitly_wait(10)
      #  self.driver.find_element(By.XPATH,self.login_username).send_keys(dem)

    #def l_password(self,dem):
     #   self.driver.find_element(By.XPATH,self.login_password).send_keys(dem)

    def l_clickbutton(self):
        wait = WebDriverWait(self.driver,20)
        we = wait.until(EC.visibility_of_element_located((By.XPATH,self.login_click_button)))
        we.click()



