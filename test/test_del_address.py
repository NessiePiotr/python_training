# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import FullName

def test_del_first_address(app):
    if app.address.count() == 0:
        app.address.add_new_element(FullName(nick_name="Test"),Birthday(),Company())
    app.address.delete_first_address()
