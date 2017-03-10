# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from address_element import FullName
from address_element import Birthday
from address_element import Company

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_address(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_address_1(self):
        success = True
        wd = self.wd
        self.home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_element(wd, FullName(first_name="First_N1", middle_name="Middle_N1", last_name="Last_N1", nick_name="Nick_N1"),
                             Birthday(day=10, month=2, year="1991"),
                             Company(company_name="Company_N1", address="Spb, Street 10", home="110", phone="+79119119191", e_mail="mail_1@mail.ru"))
        self.submit_form(wd)
        self.logout(wd)

    def test_add_address_2(self):
        success = True
        wd = self.wd
        self.home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_element(wd, FullName(first_name="First_N2", middle_name="Middle_N2", last_name="Last_N2", nick_name="Nick_N2"),
                             Birthday(day=15, month=3, year="1992"),
                             Company(company_name="Company_N2", address="Spb, Street 20", home="220", phone="+79229229292", e_mail="mail_2@mail.ru"))
        self.submit_form(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def submit_form(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def add_new_element(self, wd, full_name, birthday, company):
        wd.find_element_by_link_text("add new").click()
        # full name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(full_name.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(full_name.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(full_name.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(full_name.nick_name)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        # company name and address
        wd.find_element_by_name("company").send_keys(company.company_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(company.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(company.home)
        # phone and e-mail
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(company.phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(company.e_mail)
        # birthday
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%d]" % birthday.day).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%d]" % birthday.day).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%d]" % birthday.month).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%d]" % birthday.month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(birthday.year)

    def login(self, wd, username, password):
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
