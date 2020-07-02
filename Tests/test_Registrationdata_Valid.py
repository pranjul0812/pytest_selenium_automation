import pytest
from Utility import generate_logger as gl
import time
from allure_commons.types import AttachmentType
import allure
from Pages.registration_page import RegistrationPage


@pytest.mark.usefixtures("oneTimeSetUp")
class TestRegistrationData:
	logger = gl.custom_logger()

	@pytest.fixture(autouse=True)
	def classSetUp(self):
		self.rp = RegistrationPage(self.driver)

	@pytest.mark.second
	def test_validRegistration1(self):
		self.rp.enter_name("Pranjul")
		allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
		time.sleep(2)

	@pytest.mark.first
	def test_validRegistration2(self):
		self.rp.enter_email("pranjul0812@gmail.com")
		allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
		time.sleep(2)
