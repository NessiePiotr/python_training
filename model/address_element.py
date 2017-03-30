class FullName:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nick_name=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name


class Birthday:

    def __init__(self, day=1, month=1, year=None):
        self.day = day
        self.month = month
        self.year = year


class Company:

    def __init__(self, company_name=None, address=None, home=None, phone=None, e_mail=None):
        self.company_name = company_name
        self.address = address
        self.home = home
        self.phone = phone
        self.e_mail = e_mail