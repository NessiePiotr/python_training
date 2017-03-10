class FullName:

    def __init__(self, first_name, middle_name, last_name, nick_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name


class Birthday:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


class Company:

    def __init__(self, company_name, address, home, phone, e_mail):
        self.company_name = company_name
        self.address = address
        self.home = home
        self.phone = phone
        self.e_mail = e_mail