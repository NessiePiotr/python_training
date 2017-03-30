# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import FullName

def test_edit_address_1(app):
    if app.address.count() == 0:
        app.address.add_new_element(FullName(nick_name="Test"),Birthday(),Company())
    app.address.add_edit_element(FullName(first_name="Change First_N1", middle_name="Change Middle_N1",
                                          last_name="Change Last_N1"),
                        Birthday(day=12, month=3, year="1992"),
                        Company(company_name="Change Company_N1", address="Spb, Change Street 10", home="111", phone="+79119119199", e_mail="mail_1@mail.su"))

def test_edit_address_2(app):
    if app.address.count() == 0:
        app.address.add_new_element(FullName(nick_name="Test"),Birthday(),Company())
    app.address.add_edit_element(FullName(first_name="Change ONLY First_N1"),Birthday(),Company())
