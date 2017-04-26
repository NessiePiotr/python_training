# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import Contact
import random

def test_edit_address(app, db, check_ui):
    if len(db.get_address_list()) == 0:
        app.address.add_new_element(Contact(nick_name="Test"),Birthday(),Company())
    old_address = db.get_address_list()
    contact_to_change = random.choice(old_address)
    index_contact_to_change=old_address.index(contact_to_change)
    contact = Contact(id=contact_to_change.id, first_name="First_N2", middle_name="Middle_N2", last_name="Last_N2", nick_name="Nick_N2",
                      homephone="1101019", mobilephone="+79119119199", workphone="1100009", secondaryphone="1100019",
                      e_mail="mail_1@mail.su", address="Spb, Change Street 10"
                      )
    app.address.edit_element_by_id(contact_to_change.id, contact, Birthday(), Company())
    assert len(old_address) == app.address.count()
    old_address.remove(contact_to_change)
    old_address.insert(index_contact_to_change, contact)
    new_address = db.get_address_list()
    assert old_address == new_address
    if check_ui:
        db_list = map(app.address.clean, new_address)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.address.get_address_list(), key=Contact.id_or_max)



