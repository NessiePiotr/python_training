class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_new_element(self, full_name, birthday, company):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_fields_value(full_name, birthday, company)
        self.app.submit_form()

    def delete_first_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def add_edit_element(self, full_name, birthday, company):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_fields_value(full_name, birthday, company)
        wd.find_element_by_name("update").click()

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
        self.change_field_value("home", company.home)
        # phone and e-mail
        self.change_field_value("mobile", company.phone)
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
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))
