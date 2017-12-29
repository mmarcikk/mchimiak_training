from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

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
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[8]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[9]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[9]").click()
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

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # contact deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_editing_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//tbody/tr[2]/td[8]//img")[index].click()

    def edit_first_contact(self):
        self.delete_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_editing_contact_by_index(index)
        # edit contact
        self.fill_contact_form(new_contact_data)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[10]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[6]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[7]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[7]").click()
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
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname))
        return list(self.contact_cache)
