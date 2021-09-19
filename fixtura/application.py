from selenium import webdriver
from fixtura.session import SessionHelper
from fixtura.project import ProjectHelper
from fixtura.james import JamesHelper
from fixtura.mail import MailHelper
from fixtura.signup import SignupHelper
from fixtura.soap import SoapHelper


class Application:

    def __init__(self, browser, config):
        if browser == 'Firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'Chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.mail = MailHelper(self)
        self.signup = SignupHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.base_url = config['web']["baseUrl"]

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if wd.current_url is not self.base_url:
            wd.get(self.base_url)

    #def return_to_home_page(self):
        #wd = self.wd
        #if wd.current_url is not "http://localhost/addressbook/":
            #wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()