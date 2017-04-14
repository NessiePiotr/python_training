# -*- coding: utf-8 -*-
from model.address_element import Birthday
from model.address_element import Company
from model.address_element import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(prefix, maxlen):
    symbols = string.digits + "(" + ")" + "+" + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "@"*5 + "."*5 + "_" + "-"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
            Contact(first_name=random_string("Fname", 10), middle_name=random_string("Mname", 10),
                    last_name=random_string("Lname", 10), nick_name=random_string("Nname", 10),
                    homephone=random_phone("HP", 10), mobilephone=random_phone("MP", 10),
                    workphone=random_phone("WP", 10), secondaryphone=random_phone("SP", 10),
                    e_mail = random_email("1", 10), e_mail2 = random_email("2", 10), e_mail3 = random_email("3", 10),
                    address=random_string("Adr", 20))
            for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_address(app, contact):
    old_address = app.address.get_address_list()
    app.address.add_new_element(contact, Birthday(day=10, month=2, year="1991"),
                        Company(company_name="Company_name"))
    assert len(old_address) + 1 == app.address.count()
    new_address = app.address.get_address_list()
    old_address.append(contact)
    assert sorted(old_address, key=Contact.id_or_max) == sorted(new_address, key=Contact.id_or_max)

