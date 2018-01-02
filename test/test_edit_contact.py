from model.contact import Contact
from random import randrange


def test_edit_first_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="change")
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_first_contact_firstname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Marta"))
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="change")
#     app.contact.edit_first_contact(contact)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[0] = contact
#     assert sorted(old_contacts, key=Contact.lastname_or_max) == sorted(new_contacts, key=Contact.lastname_or_max)
#
#
# def test_edit_first_contact_email(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(email="test@gmail.com"))
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(email="martachimiak+change@gmail.com")
#     app.contact.edit_first_contact(contact)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[0] = contact
#     assert sorted(old_contacts, key=Contact.lastname_or_max) == sorted(new_contacts, key=Contact.lastname_or_max)
