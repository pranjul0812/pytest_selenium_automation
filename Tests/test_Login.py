import pytest
import allure
from allure_commons.types import AttachmentType
from EndToEndAutomation.Utility import generate_logger as gl
from EndToEndAutomation.Pages.registration_page import RegistrationPage
from ddt import unpack, data, ddt
import unittest


@ddt
@pytest.mark.usefixtures('oneTimeSetUp')
class TestLogin(unittest.TestCase):
	logger = gl.custom_logger()

	@pytest.fixture(autouse=True)
	def classSetUp(self, oneTimeSetUp):
		self.rp = RegistrationPage(self.driver)

	@data(("home", "test",), ("", ""), ("", "test"), ("testing", ""), ("test", "test",))
	@unpack
	def test_login(self, username, password,):
		try:
			self.rp.login(username, password)
		except:
			self.logger.error("Login Fail, Login button element can't be found")
			allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot_error', attachment_type=AttachmentType.PNG)
			assert 1 == 2

		if username == 'test' and password == 'test':
			if self.rp.verifyLogin():
				allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
				self.logger.info("Login Success")
			else:
				allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot_error', attachment_type=AttachmentType.PNG)
				self.logger.error("Login Fail")
				assert 1 == 2
		else:
			if self.rp.verifyLogin():
				allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot_error', attachment_type=AttachmentType.PNG)
				self.logger.error("Login should Fail but it is passed")
				assert 1 == 2
			else:
				allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
				self.logger.info("Login Fails as Expected")





