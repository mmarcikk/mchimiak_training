from model.contact import Contact
import getopt
import jsonpickle
import os.path
import random
import string
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", home="", mobile="", work="", phone2="", address="", email="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 5), home=random_string("home", 9), mobile=random_string("mobile", 9),
          work=random_string("work", 9), phone2=random_string("phone2", 9), address=random_string("address", 20), email=random_string("email", 5) + "@" + random_string("", 4) + "." + random_string("",3),
          email2=random_string("email2", 5) + "@" + random_string("", 4) + "." + random_string("",3), email3=random_string("email3", 5) + "@" + random_string("", 4) + "." + random_string("",3))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
