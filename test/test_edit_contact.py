from model.contact import Contact


def test_edit_first_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(title="test"))
    app.contact.edit_first_contact(Contact(title="change"))


def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marta"))
    app.contact.edit_first_contact(Contact(firstname="change"))


def test_edit_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(email="test@gmail.com"))
    app.contact.edit_first_contact(Contact(email="martachimiak+change@gmail.com"))
