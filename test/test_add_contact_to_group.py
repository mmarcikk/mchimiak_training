# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test name"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    old_contacts_in_group = db.get_contacts_not_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group = db.get_contacts_not_in_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)
