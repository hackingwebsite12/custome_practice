import pytest
from selenium import webdriver
from pageobjects.class_register import register_page
from pageobjects.class_store import admin_entering
from pageobjects.class_tut_capmes import capmes

@pytest.mark.skip
class Test_reg:

    def test_calling_register_page(self,setupcon):
        self.driver = setupcon
        self.driver.get("https://www.opencart.com/index.php?route=account/register")
        clr = register_page(self.driver)
        #clr.move_register_page()
        clr.user_name("Vairatha")
        clr.first_name("vairathareddy")
        clr.last_name("reddy")
        clr.e_mail("20514149s@gmail.com")
        clr.pass_word("Vairatha@123")
        clr.countries()
        clr.reg_but()


class Test_admin:

    def test_admin_calling(self,setupcon):
        self.driver = setupcon
        self.driver.get("https://www.opencart.com/index.php?route=cms/demo")
        adm=admin_entering(self.driver)
        adm.admin_opening()
       # adm.l_username("demo")
        #adm.l_password("demo")
        adm.l_clickbutton()


