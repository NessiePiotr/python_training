# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import FullName

def test_del_first_address(app):
    if app.address.count() == 0:
        app.address.add_new_element(FullName(nick_name="Test"),Birthday(),Company())
    old_address = app.address.get_address_list()
    app.address.delete_first_address()
    new_address = app.address.get_address_list()
    assert len(old_address) - 1 == len(new_address)
    old_address[0:1] = []
    assert old_address == new_address
