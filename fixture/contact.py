from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill in the form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # contact deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # contact deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_editing_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def select_editing_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("a[href*='edit.php?id=%s']" % id).click()

    def select_view_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def edit_first_contact(self):
        self.delete_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_editing_contact_by_index(index)
        # edit contact
        self.fill_contact_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update'][2]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.select_editing_contact_by_id(id)
        # edit contact
        self.fill_contact_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update'][2]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page = all_phones, id=id))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_editing_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, mobile=mobile, work=work,
                       phone2=phone2, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.select_view_contact_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)

    def add_contact_to_group(self, group):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact by id
        self.select_contact_by_id(id)
        # add contact to group
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_css_selector("option[value='%s']" % group.id).click()
        wd.find_element_by_name("add").click()
        # go to contact list from added group
        wd.find_element_by_partial_link_text("group_page").click()
        self.contact_cache = None

    def delete_contact_from_group(self, group):
        wd = self.app.wd
        self.app.open_home_page()
        # select group
        wd.find_element_by_name("group").click()
        wd.find_element_by_css_selector("option[value=\"%s\"]" % group.id).click()
        # select contact by id
        self.select_contact_by_id(id)
        # remove contact from group
        wd.find_element_by_name("remove").click()
        # go to contact list from deleted group
        wd.find_element_by_partial_link_text("group_page").click()
        self.contact_cache = None

























