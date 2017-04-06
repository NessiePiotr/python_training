# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="Change First_group", header="Change Start first_group", footer="Change End first_group")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(name="Change First_group"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(header="Change Start first_group"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)