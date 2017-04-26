from model.address_element import Birthday
from model.address_element import Company
from model.address_element import Contact

def test_add_address(app, db, check_ui, json_contacts):
    contact = json_contacts
    old_address = db.get_address_list()
    app.address.add_new_element(contact, Birthday(day=10, month=2, year="1991"),
                        Company(company_name="Company_name"))
    new_address = db.get_address_list()
    old_address.append(contact)
    assert sorted(old_address, key=Contact.id_or_max) == sorted(new_address, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(app.address.clean, new_address), key=Contact.id_or_max) == sorted(app.address.get_address_list(), key=Contact.id_or_max)

