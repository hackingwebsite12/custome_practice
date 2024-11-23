import time

import selenium.webdriver.support.expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import webdriver_manager.drivers.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import pytest

class Test_makemytrip:

    def setup_method(self):
        opt = Options()
        opt.add_argument("--disable-blink-features=AutomationControlled")
        opt.add_argument("--disable-infobars")
        opt.add_argument("--start-maximized")
        opt.add_experimental_option("excludeSwitches", ["enable-automation"])
        #opt.add_experimental_option("useAutomationExtension", False)
        #opt.add_argument("--incognito")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
    @pytest.mark.skip
    def test_tc01(self):
        self.driver.get("https://www.makemytrip.com/flights/")
        self.driver.implicitly_wait(10)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//a[@class='headerIcons makeFlex hrtlCenter column active']").click()
        self.driver.find_element(By.XPATH,"//div//li[@data-cy='roundTrip']").click()
        wait = WebDriverWait(self.driver,10)
        #wait = self.driver.find_element(By.XPATH,"//input[@id='departure']").click()
        we = wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[@class='lbl_input appendBottom10'])[3]")))
        we.click()
        time.sleep(10)
        we = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='dateFiled active']")))
        we.click()
        #self.driver.find_element(By.XPATH,"//div[@class='dateFiled active']").click()
        self.driver.find_element(By.XPATH,"//div[@aria-label='Fri Nov 08 2024']//p[contains(text(),'8')]").click()
        self.driver.find_element(By.XPATH,"//div[@aria-label='Wed Nov 20 2024']//div[@class='dateInnerCell']").click()
        self.driver.find_element(By.XPATH,"//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']").click()
        self.driver.close()
    @pytest.mark.skip
    def test_tc02(self):
        self.driver.get("https://www.makemytrip.com/flight/search?itinerary=DEL-BOM-09/11/2024&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng&cmp=SEM|D|DF|B|Brand|Brand-BrandExact_DT|B_M_Makemytrip_Search_Exact|Brand_Top_5_Exact|RSA|")
        time.sleep(5)
        try:
            wait = WebDriverWait(self.driver,10)
            we = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[contains(@class,'bgProperties overlayCrossIcon icon20')]")))
            we.click()
        except TimeoutException:
            print("the overlay button not present")
        #self.driver.find_element(By.XPATH,"//span[contains(@class,'bgProperties overlayCrossIcon icon20')]").click()
        time.sleep(10)
        try:
            wait = WebDriverWait(self.driver,15)
            we = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='GOT IT']")))
            we.click()
        except TimeoutException:
            print("got it button not found")
        wait = WebDriverWait(self.driver,20)
        li = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//p[contains(@class,'boldFont blackText')]")))
        li1 = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'flexOne')]")))
        dic = dict(zip(li,li1))
        for k,v in dic.items():
            print(k.text,v.text,end='\t')
            #s = i.text
            #print(s)
    @pytest.mark.skip
    def test_tc03(self):
        self.driver.get("")
        we = self.driver.execute_script("return document.getElementsByClassName('rangeslider__handle-label')[0];")
        Act = ActionChains(self.driver)
        Act.click_and_hold(we).move_by_offset(24600, 18000).release().perform()
        li = self.driver.find_elements(By.XPATH, "//div[@class='blackText fontSize18 blackFont white-space-no-wrap clusterViewPrice']")
        nli=[]
        for i in li:
            al = i.text.replace(',','')
            nli.append(int(al))
        print(nli.sort())
    @pytest.mark.skip
    def test_tc04(self):
        self.driver.get("")
        self.driver.find_element(By.XPATH,"//div//p[.=' 1 Stop   ']").click()
        time.sleep(5)
        li = self.driver.find_elements(By.XPATH,"//p//font[contains(text(),'1 stop')]")
        for i in li:
            s = i.text
            ns = '1 stop'
            if ns in s:
                assert True
                print("filtering is working")
    @pytest.mark.skip
    def test_tc05(self):
        self.driver.get("https://www.makemytrip.com/flight/search?itinerary=DEL-BOM-09/11/2024&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng")
        try:
            wait = WebDriverWait(self.driver,15)
            we = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='GOT IT']")))
            we.click()
        except TimeoutException:
            print("there is an element unidentified")
        self.driver.find_element(By.XPATH,"(//p[contains(text(),'Non Stop')])[2]").click()
        self.driver.find_element(By.XPATH,"(//p[normalize-space()='1 Stop'])[1]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//p[normalize-space()='Air India Express']//span[@class='appendRight5 icon12 bgProperties']").click()
        time.sleep(5)
        wait = WebDriverWait(self.driver,10)
        we = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='linkText ctaLink viewFltDtlsCta']")))
        we.click()
        wait = WebDriverWait(self.driver, 20)
        li = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='baggageInfo']/descendant::span[contains(@class,'darkText')]")))
        for i in li:
            s = i.text
            req_val = ['15 Kgs (1 piece only)',' ADULT', '7 Kgs']
            if all(val in s for val in req_val):
                print("validation done")
                assert True

    @pytest.mark.skip
    def test_tc06(self):
        self.driver.get("https://www.makemytrip.com/hotels/")
        self.driver.implicitly_wait(10)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[@class='commonModal__close']").click()
        self.driver.find_element(By.XPATH,"//input[@data-cy='city']").click()
        try:
           self.driver.find_element(By.XPATH,"//input[@placeholder='Where do you want to stay?']")
        except NoSuchElementException:
            wait = WebDriverWait(self.driver,20)
            we = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Where do you want to stay?']")))
            we.send_keys("Goa")
        self.driver.find_element(By.XPATH,"//input[@id='checkin']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//div[@aria-label='Sun Nov 17 2024']").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='Tue Nov 19 2024']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "(//input[@id='guest'])[1]").click()
        time.sleep(5)
        wait = WebDriverWait(self.driver,10)
        we = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"gstSlct")))
        self.driver.execute_script("arguments[0].value=2;",we)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Apply']").click()
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Price per Night']").click()
        self.driver.find_element(By.XPATH,"(//li[contains(text(),'₹1500')])[2]").click()
        self.driver.find_element(By.XPATH,"//button[@id='hsw_search_button']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//span[contains(text(),'Book with ₹0 Payment')])[1]").click()
        time.sleep(5)

    @pytest.mark.skip
    def test_tc07(self):
        self.driver.get("https://demo.guru99.com/test/web-table-element.php")
        li = self.driver.find_elements(By.XPATH,"//table//tbody//tr[last()]")
        for i in li:
           vals =  i.find_elements(By.TAG_NAME,"td")
           for v in vals:
               print(v.text)
    @pytest.mark.skip
    def test_tc08(self):
        self.driver.get("https://demo.guru99.com/test/web-table-element.php")
        nl = self.driver.find_elements(By.XPATH,"//table//tbody//td[position()=4]")
        va = []
        for i in nl:
            va.append(int(i.text.replace('.','')))
        sval = sorted(va)
        assert va == sval, "sorted"
    @pytest.mark.skip
    def test_tc09(self):
        self.driver.get("https://seleniumpractise.blogspot.com/2021/08/webtable-in-html.html")
        al_rs = self.driver.find_elements(By.XPATH,"//table//tbody//tr")
        for i in al_rs:
            rd = i.find_elements(By.XPATH,"td")
            for r in rd:
                if r.text == 'Ola':
                    rd[4].click()
    @pytest.mark.skip
    def test_tc10(self):
        self.driver.get("https://demo.guru99.com/test/web-table-element.php")
        nl = self.driver.find_elements(By.XPATH,"//table//tbody//tr")
        lr = []
        rcount = 0
        for rn in nl:
            rd = rn.find_elements(By.XPATH,"td")
            for r in rd:
                if '+8.9' == r.text:
                    rcount+=1
                print(rd[1].text,"\t the count is:", rcount)
    @pytest.mark.skip
    def test_tc11(self):
        self.driver.get("https://seleniumpractise.blogspot.com/2021/08/webtable-in-html.html")
        li = self.driver.find_elements(By.XPATH,"//table//tbody//td[last()]/a")
        for i in li:
            va = i.get_attribute("href")
            print(va)

    @pytest.mark.skip
    def test_tc12(self):
        self.driver.get("https://seleniumpractise.blogspot.com/2019/09/bootstrap-tooltip-in-selenium.html#")
        tp = (self.driver.find_element(By.XPATH,"//div//a[text()='Hover over me']"))
        act = ActionChains(self.driver)
        act.move_to_element(tp).perform()
        print(tp.get_attribute("data-original-title"))
    @pytest.mark.skip
    def test_tc13(self):
        self.driver.get("https://www.amazon.in/s?k=samsung+mobile+5%2Bg&crid=2CZMA30MUDULX&sprefix=samsung+mo%2Caps%2C376&ref=nb_sb_ss_ts-doa-p_1_10")
        li = self.driver.find_elements(By.XPATH,"//div[@data-cy='title-recipe']")
        button = self.driver.find_element(By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
        time.sleep(5)
        elli = []
        for i in li:
            elli.append(i.text)
        while "disable" not in button.get_attribute("class"):
            button.click()
            wait = WebDriverWait(self.driver,10)
            wait.until(EC.staleness_of(button))
            li = self.driver.find_elements(By.XPATH, "//div[@data-cy='title-recipe']")
            for i in li:
                elli.append(i.text)
            button = wait.until(EC.visibility_of_element_located((By.XPATH,
                                              "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")))

        for j in elli:
            print(j)

    @pytest.mark.skip
    def test_tc14(self):
        self.driver.get("https://demo.guru99.com/test/web-table-element.php")
        li = self.driver.find_elements(By.XPATH,"//table//tbody//td[position()=3 or position()=4]")

        ns = set()
        for i in li:
            ns.add(i.text)
        print(len(li),len(ns))
        print(ns)

    def test_tc15(self):
        self.driver.get("https://www.amazon.in/s?k=samsung+mobile+5%2Bg&i=electronics&crid=2XS1UEN795S6V&sprefix=%2Celectronics%2C264&ref=nb_sb_ss_recent_1_0_recent")
        self.driver.implicitly_wait(10)
        check_filter = ['Samsung','Redmi','Motorola']
        li = []
        li = self.driver.find_elements(By.XPATH,"//span[@class='a-size-base a-color-base']")
        for i in li:
            if i.text in check_filter:
                i.click()
                print(i.text)
                time.sleep(5)
            li = self.driver.find_elements(By.XPATH,"//span[@class='a-size-base a-color-base']")

    def test_tc16(self):
        self.driver.get("https://www.amazon.in/s?k=samsung+mobile+5%2Bg&i=electronics&rh=n%3A976419031&dc&crid=2XS1UEN795S6V&qid=1731661427&rnid=91049095031&sprefix=%2Celectronics%2C264&ref=sr_nr_p_123_1&ds=v1%3AfEHJsRlx3ytFPZe5xqfA2MhWMPBvWZ8qodPmaJbUkJo")
        li = self.driver.find_elements(By.XPATH,"//div//span[contains(text(),'Samsung Galaxy')]")
        te = 'M15 5G Prime Edition'
        for i in li:
            if te in i.text:
                i.click()
                time.sleep(3)
#//div[@class='a-section a-spacing-none aok-align-center aok-relative']//span[@class='a-price-whole']
        wh = self.driver.window_handles
        self.driver.switch_to.window(wh[2])
        time.sleep(4)
        pr = self.driver.find_element(By.XPATH,"//div[@class='a-section a-spacing-none aok-align-center aok-relative']//span[@class='a-price-whole']")
        print(self.driver.current_window_handle.title,pr.text)
        time.sleep(4)
        self.driver.switch_to.default_content()











