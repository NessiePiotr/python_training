from pony.orm import *
from datetime import datetime
from model.group import Group
from model.address_element import Contact
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        last_name = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, database, user, password):
        self.db.bind('mysql', host=host, database=database, user=user, password=password, conv=decoders)
        self.db.generate_mapping()

    def conver_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def conver_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), first_name=contact.first_name, last_name=contact.last_name)
        return list(map(convert, contacts))

    def get_group_list(self):
        return self.conver_groups_to_model((select (g for g in ORMFixture.ORMGroup)))

    def get_address_list(self):
        return self.conver_contacts_to_model((select (c for c in ORMFixture.ORMContact if c.deprecated is None)))

