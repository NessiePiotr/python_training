# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="Change First_group", header="Change Start first_group", footer="Change End first_group"))

def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="Change First_group"))

def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="Change Start first_group"))
