# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Marta", middlename="Katarzyna", lastname="Chimiak",
                        nickname="marcik", title="klient", company="google", address="ul. Dluga 55 Poznan",
                        home="61222222", mobile="666555666", work="666111666", fax="666111222",
                        email="martachimiak@gmail.com", email2="test@gmail.com", email3="test2@gmail.com",
                        homepage="www.test.pl", byear="1990", address2="ul. Kręta 66, Poznan", ayear="2014",
                        phone2="Poland", notes="text"))
    app.logout()
