# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import FullName

def test_edit_address_1(app):
    if app.address.count() == 0:
        app.address.add_new_element(FullName(nick_name="Test"),Birthday(),Company())
    old_address = app.address.get_address_list()
    fullname = FullName(first_name="First_N2", middle_name="Middle_N2", last_name="Last_N2", nick_name="Nick_N2")
    fullname.id = old_address[0].id
    app.address.add_edit_element(fullname, Birthday(day=12, month=3, year="1992"),
                        Company(company_name="Change Company_N1", address="Spb, Change Street 10", home="111", phone="+79119119199", e_mail="mail_1@mail.su"))
    new_address = app.address.get_address_list()
    assert len(old_address) == len(new_address)
    old_address[0] = fullname
    assert sorted(old_address, key=FullName.id_or_max) == sorted(new_address, key=FullName.id_or_max)


# def test_edit_address_2(app):
#     if app.address.count() == 0:
#         app.address.add_new_element(FullName(nick_name="Test"),Birthday(),Company())
#     app.address.add_edit_element(FullName(first_name="Change ONLY First_N1"),Birthday(),Company())