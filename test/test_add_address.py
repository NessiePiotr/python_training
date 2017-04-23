# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import Contact
import pytest

def test_add_address(app, json_contacts):
    contact = json_contacts
    old_address = app.address.get_address_list()
    app.address.add_new_element(contact, Birthday(day=10, month=2, year="1991"),
                        Company(company_name="Company_name"))
    assert len(old_address) + 1 == app.address.count()
    new_address = app.address.get_address_list()
    old_address.append(contact)
    assert sorted(old_address, key=Contact.id_or_max) == sorted(new_address, key=Contact.id_or_max)

