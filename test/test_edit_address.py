# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import FullName

def test_edit_address(app):
    app.address.add_edit_element(FullName(first_name="Change First_N1", middle_name="Change Middle_N1",
                                          last_name="Change Last_N1", nick_name="Change Nick_N1"),
                        Birthday(day=12, month=3, year="1992"),
                        Company(company_name="Change Company_N1", address="Spb, Change Street 10", home="111", phone="+79119119199", e_mail="mail_1@mail.su"))
