# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import Contact
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")

def test_del_some_address(app, check_ui):
    if len(db.get_address_list()) == 0:
        app.address.add_new_element(Contact(nick_name="Test"),Birthday(),Company())
    old_address = db.get_address_list()
    address = random.choice(old_address)
    app.address.delete_address_by_id(address.id)
    old_address.remove(address)
    new_address = db.get_address_list()
    assert old_address == new_address
    if check_ui:
        db_list = map(app.address.clean, new_address)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.address.get_address_list(), key=Contact.id_or_max)
