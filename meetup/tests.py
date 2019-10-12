import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(LoginTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase, self).tearDown()

    def test_login(self):
        selenium = self.selenium

        selenium.get('http://127.0.0.1:8000/user_login/')

        email = selenium.find_element_by_id('id_email')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_name('login')

        email.send_keys('member@member.com')
        password.send_keys('adminadmin')
        submit.send_keys(Keys.RETURN)

        assert '.' in selenium.page_source

class SignupTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(SignupTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SignupTestCase, self).tearDown()

    def test_signup(self):
        selenium = self.selenium

        selenium.get('http://127.0.0.1:8000/register/')

        name = selenium.find_element_by_id('id_name')
        email = selenium.find_element_by_id('id_email')
        interest1 = selenium.find_element_by_id('id_interests_0')
        interest2 = selenium.find_element_by_id('id_interests_1')
        password = selenium.find_element_by_id('id_password1')
        host = selenium.find_element_by_id('id_host')
        password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_element_by_name('submit')

        name.send_keys('ADmin USer')
        email.send_keys('dkvhwbdvbwdio')
        interest1.send_keys(Keys.RETURN)
        interest2.send_keys(Keys.RETURN)
        host.send_keys(Keys.RETURN)
        password.send_keys('adminadmin')
        password2.send_keys('adminadmin')
        submit.send_keys(Keys.RETURN)

        assert '.' in selenium.page_source

