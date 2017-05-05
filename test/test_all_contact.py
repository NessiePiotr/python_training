import re
import random


def test_phones_on_home_page(app, db):
    contact_from_db = db.get_address_list()
    contact_from_home_page = app.address.get_address_list()
    for contact_from_db_to_check in contact_from_db:
        for contact_from_home_page_to_check in contact_from_home_page:
            if contact_from_db_to_check == contact_from_home_page_to_check:
                assert contact_from_home_page_to_check.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db_to_check)
                assert contact_from_home_page_to_check.all_e_mails_from_home_page == merge_e_mails_like_on_home_page(contact_from_db_to_check)
                assert contact_from_home_page_to_check.address == contact_from_db_to_check.address.strip()

def clear(s):
    return re.sub("[() -]", "" , s)

def clear_email(s):
    return re.sub(" ", "" , s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_e_mails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                       [contact.e_mail, contact.e_mail2, contact.e_mail3]))))