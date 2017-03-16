from selenium.webdriver.firefox.webdriver import WebDriver

class Address_appl:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def submit_form(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def add_new_element(self, full_name, birthday, company):
        wd = self.wd
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
        self.submit_form()

    def login(self, username, password):
        wd = self.wd
        self.home_page()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
