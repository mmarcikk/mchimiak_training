# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", home="", mobile="", work="", phone2="", address="", email="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 5), home=random_string("home", 9), mobile=random_string("mobile", 9),
          work=random_string("work", 9), phone2=random_string("phone2", 9), address=random_string("address", 20), email=random_string("email", 5) + "@" + random_string("", 4) + "." + random_string("",3),
          email2=random_string("email2", 5) + "@" + random_string("", 4) + "." + random_string("",3), email3=random_string("email3", 5) + "@" + random_string("", 4) + "." + random_string("",3))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
