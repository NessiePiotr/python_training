# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Change First_group", header="Change Start first_group", footer="Change End first_group"))
    app.session.logout()


