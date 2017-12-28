from model.contact import Contact


def test_edit_first_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(title="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(title="change")
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.lastname_or_max) == sorted(new_contacts, key=Contact.lastname_or_max)


def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marta"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="change")
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.lastname_or_max) == sorted(new_contacts, key=Contact.lastname_or_max)


def test_edit_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(email="test@gmail.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(email="martachimiak+change@gmail.com")
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.lastname_or_max) == sorted(new_contacts, key=Contact.lastname_or_max)