import pytest
from pageobjects.class_tut_capmes import capmes

@pytest.mark.sanity
class Test_tutocalling:

    def test_call_tot(self,setupcon):
        self.driver = setupcon
        self.driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
        tc = capmes(self.driver)
        tc.last_name("reddy")
        tc.first_name("anush")
        tc.new_pass("anush@123")
        tc.confirm_pas("anush@123")
        tc.email("20414")
        tc.confirm_but()

