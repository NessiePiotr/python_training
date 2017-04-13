from model.address_element import FullName
import re

class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_new_element(self, full_name, birthday, company):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_fields_value(full_name, birthday, company)
        self.app.submit_form()
        self.address_cache = None

    def delete_first_address(self):
        self.delete_address_by_index(0)

    def delete_address_by_index(self, index):
        wd = self.app.wd
        self.go_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.address_cache = None

    def add_edit_element(self, full_name, birthday, company):
        edit_element_by_index(0, full_name, birthday, company)

    def edit_element_by_index(self, index, full_name, birthday, company):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_fields_value(full_name, birthday, company)
        wd.find_element_by_name("update").click()
        self.address_cache = None

    def change_field_value(self, name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(name).click()
            wd.find_element_by_name(name).clear()
            wd.find_element_by_name(name).send_keys(value)

    def fill_fields_value(self, full_name, birthday, company):
        wd = self.app.wd
        # full name
        self.change_field_value("firstname", full_name.first_name)
        self.change_field_value("middlename", full_name.middle_name)
        self.change_field_value("lastname", full_name.last_name)
        self.change_field_value("nickname", full_name.nick_name)
        # company name and address
        self.change_field_value("company", company.company_name)
        self.change_field_value("address", company.address)
        # phone and e-mail
        self.change_field_value("home", full_name.homephone)
        self.change_field_value("mobile", full_name.mobilephone)
        self.change_field_value("work", full_name.workphone)
        self.change_field_value("phone2", full_name.secondaryphone)
        self.change_field_value("email", company.e_mail)
        # birthday
        if birthday.day is not None:
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%d]" % birthday.day).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%d]" % birthday.day).click()
        if birthday.month is not None:
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%d]" % birthday.month).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%d]" % birthday.month).click()
        self.change_field_value("byear", birthday.year)

    def count(self):
        wd = self.app.wd
        self.go_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def go_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("MainForm")) > 0):
            wd.find_element_by_link_text("home").click()

    address_cache = None

    def get_address_list(self):
        if self.address_cache is None:
            wd = self.app.wd
            self.go_home_page()
            self.address_cache = []
            for element in wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[@name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cell = element.find_elements_by_tag_name("td")
                text_LN = cell[1].text
                text_FN = cell[2].text
                all_phones = cell[5].text.splitlines()
                self.address_cache.append(FullName(first_name=text_FN, last_name=text_LN, id=id,
                                                   homephone=all_phones[0], mobilephone=all_phones[1],
                                                   workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.address_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.go_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_address_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return FullName(first_name=firstname, last_name=lastname, id=id,
                         homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def get_address_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return FullName(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)






