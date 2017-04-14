from sys import maxsize

class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nick_name=None, id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, address=None,
                 all_phones_from_home_page=None, e_mail=None, e_mail2=None, e_mail3=None, all_e_mails_from_home_page=None):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.address = address
        self.e_mail = e_mail
        self.e_mail2 = e_mail2
        self.e_mail3 = e_mail3
        self.all_e_mails_from_home_page = all_e_mails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.first_name, self.last_name, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

class Birthday:

    def __init__(self, day=1, month=1, year=None):
        self.day = day
        self.month = month
        self.year = year

class Company:

    def __init__(self, company_name=None):
        self.company_name = company_name
