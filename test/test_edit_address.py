# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import Contact
from random import randrange

def test_edit_address(app):
    if app.address.count() == 0:
        app.address.add_new_element(Contact(nick_name="Test"),Birthday(),Company())
    old_address = app.address.get_address_list()
    index = randrange(len(old_address))
    contact = Contact(first_name="First_N2", middle_name="Middle_N2", last_name="Last_N2", nick_name="Nick_N2",
                      homephone="1101019", mobilephone="+79119119199", workphone="1100009", secondaryphone="1100019",
                      e_mail="mail_1@mail.su", address="Spb, Change Street 10"
                      )
    contact.id = old_address[index].id
    app.address.edit_element_by_index(index, contact, Birthday(day=12, month=3, year="1992"),
                        Company(company_name="Change Company_N1"))
    assert len(old_address) == app.address.count()
    new_address = app.address.get_address_list()
    old_address[index] = contact
    assert sorted(old_address, key=Contact.id_or_max) == sorted(new_address, key=Contact.id_or_max)


# def test_edit_address_2(app):
#     if app.address.count() == 0:
#         app.address.add_new_element(Contact(nick_name="Test"),Birthday(),Company())
#     app.address.add_edit_element(Contact(first_name="Change ONLY First_N1"),Birthday(),Company())
