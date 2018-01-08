# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random

def test_delete_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test name"))
    groups = db.get_group_list()
    group = random.choice(groups)
    old_contacts_in_group = db.get_contacts_not_in_group(group)
    contact_in_group = random.choice(old_contacts_in_group)
    if len(old_contacts_in_group) == 0:
        contacts = db.get_contacts_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group(contact, group)
    app.contact.delete_contact_from_group(contact_in_group)
    new_contacts_in_group = db.get_contacts_in_group(group)
    old_contacts_in_group.remove(contact_in_group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)