from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="change", middlename="change", lastname="change",
                                   nickname="change", title="change", company="change", address="ul. Dluga 55 Change",
                                   home="111111111", mobile="222222222", work="333333333", fax="444444444",
                                   email="martachimiak+change@gmail.com", email2="test+change@gmail.com",
                                   email3="test2+change@gmail.com", homepage="www.change.pl", byear="1990",
                                   address2="ul. Kręta 66, Change", ayear="2011", phone2="Germany", notes="change"))
    app.session.logout()
