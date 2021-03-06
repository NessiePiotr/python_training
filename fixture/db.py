import mysql.connector
from model.group import Group
from model.address_element import Contact

class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=str(name), header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_address_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), first_name=str(firstname), last_name=str(lastname), address=str(address),
                                    homephone=str(home), mobilephone=str(mobile), workphone=str(work), secondaryphone=str(phone2),
                                    e_mail=str(email), e_mail2=str(email2), e_mail3=str(email3)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

