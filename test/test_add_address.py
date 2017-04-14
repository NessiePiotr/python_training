# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import Contact

def test_add_address(app):
    old_address = app.address.get_address_list()
    contact = Contact(first_name="First_N1", middle_name="Middle_N1", last_name="Last_N1", nick_name="Nick_N1",
                      homephone="1101010", mobilephone="+79119119191", workphone="1100000", secondaryphone="1100010",
                      e_mail = "mail_1@mail.ru", address="Spb, Street 10")
    app.address.add_new_element(contact, Birthday(day=10, month=2, year="1991"),
                        Company(company_name="Company_N1"))
    assert len(old_address) + 1 == app.address.count()
    new_address = app.address.get_address_list()
    old_address.append(contact)
    assert sorted(old_address, key=Contact.id_or_max) == sorted(new_address, key=Contact.id_or_max)

