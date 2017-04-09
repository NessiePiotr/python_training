# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import FullName
from random import randrange


def test_del_first_address(app):
    if app.address.count() == 0:
        app.address.add_new_element(FullName(nick_name="Test"),Birthday(),Company())
    old_address = app.address.get_address_list()
    index = randrange(len(old_address))
    app.address.delete_address_by_index(index)
    assert len(old_address) - 1 == app.address.count()
    new_address = app.address.get_address_list()
    old_address[index:index+1] = []
    assert old_address == new_address
