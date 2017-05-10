# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import Contact
import random

def test_del_some_address(app, orm, check_ui):
    if len(orm.get_address_list()) == 0:
        app.address.add_new_element(Contact(nick_name="Test"),Birthday(),Company())
    old_address = orm.get_address_list()
    address = random.choice(old_address)
    app.address.delete_address_by_id(address.id)
    old_address.remove(address)
    new_address = orm.get_address_list()
    assert old_address == new_address
    if check_ui:
        db_list = map(app.address.clean, new_address)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.address.get_address_list(), key=Contact.id_or_max)
