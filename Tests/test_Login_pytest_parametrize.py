import pytest
import allure
from allure_commons.types import AttachmentType
from Utility import generate_logger as gl
from Pages.registration_page import RegistrationPage


def dataGenerator():
	li = [("home", "test",), ("", ""), ("", "test"), ("testing", ""), ("test", "test",)]
	return li


@pytest.mark.usefixtures('oneTimeSetUp')
class TestLogin:
	logger = gl.custom_logger()

	@pytest.fixture(autouse=True)
	def classSetUp(self, oneTimeSetUp):
		self.rp = RegistrationPage(self.driver)

	@pytest.mark.parametrize('data', dataGenerator())
	def test_login(self, data):
		try:
			self.rp.login(data[0], data[1])
		except:
			self.logger.error("Login Fail, Login button element can't be found")
			allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot_error', attachment_type=AttachmentType.PNG)
			assert 1 == 2

		if data[0] == 'test' and data[1] == 'test':
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





