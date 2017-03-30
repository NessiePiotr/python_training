# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="First_group", header="Start first_group", footer="End first_group"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

