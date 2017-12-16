from model.contact import Contact


def test_edit_first_contact_title(app):
    app.contact.edit_first_contact(Contact(title="change"))


def test_edit_first_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="change"))


def test_edit_first_contact_email(app):
    app.contact.edit_first_contact(Contact(email="martachimiak+change@gmail.com"))
