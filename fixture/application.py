from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},
            firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def destroy(self):
        self.wd.quit()
