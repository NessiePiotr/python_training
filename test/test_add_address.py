# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import FullName

def test_add_address_1(app):
    app.address.add_new_element(FullName(first_name="First_N1", middle_name="Middle_N1", last_name="Last_N1", nick_name="Nick_N1"),
                        Birthday(day=10, month=2, year="1991"),
                        Company(company_name="Company_N1", address="Spb, Street 10", home="110", phone="+79119119191", e_mail="mail_1@mail.ru"))

def test_add_address_2(app):
    app.address.add_new_element(FullName(first_name="First_N2", middle_name="Middle_N2", last_name="Last_N2", nick_name="Nick_N2"),
                        Birthday(day=15, month=3, year="1992"),
                        Company(company_name="Company_N2", address="Spb, Street 20", home="220", phone="+79229229292", e_mail="mail_2@mail.ru"))

def test_add_address_3(app):
    app.address.add_new_element(FullName(first_name="First_N3", middle_name="Middle_N3", last_name="Last_N3"),
                        Birthday(),
                        Company(address="Spb, Street 30", home="330", phone="+79339339393", e_mail="mail_3@mail.ru"))
