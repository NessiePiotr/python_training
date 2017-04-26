from model.group import Group
import random

def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group_to_change = random.choice(old_groups)
    index_group_to_change = old_groups.index(group_to_change)
    group = Group(id=group_to_change.id, name="Change First_group", header="Change Start first_group", footer="Change End first_group")
    app.group.edit_group_by_id(group_to_change.id, group)
    old_groups.remove(group_to_change)
    old_groups.insert(index_group_to_change, group)
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(map(app.group.clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)