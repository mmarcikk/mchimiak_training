# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Marta", lastname="Chimiak", home="61222222", mobile="666555666", work="666111666",
                      phone2="111222333")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.lastname_or_max) == sorted(new_contacts, key=Contact.lastname_or_max)
