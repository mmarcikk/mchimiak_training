from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, home=None, mobile=None, work=None, phone2=None, id=None, all_phones_from_home_page=None, email=None, email2=None, email3=None, address=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def lastname_or_max(self):
        if self.lastname:
            return str(self.lastname)
        else:
            return str(maxsize)