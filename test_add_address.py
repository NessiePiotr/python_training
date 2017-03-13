# -*- coding: utf-8 -*-
import pytest
from Address_appl import Address_appl
from address_element import FullName
from address_element import Birthday
from address_element import Company

@pytest.fixture
def app(request):
    fixture = Address_appl()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_address_1(app):
    app.login(username="admin", password="secret")
    app.add_new_element(FullName(first_name="First_N1", middle_name="Middle_N1", last_name="Last_N1", nick_name="Nick_N1"),
                        Birthday(day=10, month=2, year="1991"),
                        Company(company_name="Company_N1", address="Spb, Street 10", home="110", phone="+79119119191", e_mail="mail_1@mail.ru"))
    app.logout()

def test_add_address_2(app):
    app.login(username="admin", password="secret")
    app.add_new_element(FullName(first_name="First_N2", middle_name="Middle_N2", last_name="Last_N2", nick_name="Nick_N2"),
                        Birthday(day=15, month=3, year="1992"),
                        Company(company_name="Company_N2", address="Spb, Street 20", home="220", phone="+79229229292", e_mail="mail_2@mail.ru"))
    app.logout()
