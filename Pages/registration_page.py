from selenium.webdriver.common.by import By
from Utility import generate_logger as gl
from Utility import configreader as cr
import time


class RegistrationPage:
	logger = gl.custom_logger()

	def __init__(self, driver):
		self.driver = driver

	def enter_name(self, name):
		self.driver.find_element_by_name(cr.getElementLocators('Registration', 'username_name')).send_keys(name)
		self.logger.info(name + " is set as name")

	def enter_email(self, email):
		self.driver.find_element_by_name(cr.getElementLocators('Registration', 'email_name')).send_keys(email)
		self.logger.info(email + " is filled in Email field")

	def click_login_tab(self):
		self.driver.find_element(By.XPATH, cr.getElementLocators('Login', 'login_tab_xpath')).click()
		self.logger.info("Login tab is clicked.")

	def enter_username(self, username):
		self.driver.find_element(By.XPATH, cr.getElementLocators('Login', 'username_xpath')).send_keys(username)
		self.logger.info("Username is entered: " + username)

	def enter_password(self, password):
		self.driver.find_element(By.XPATH, cr.getElementLocators('Login', 'pwd_xpath')).send_keys(password)
		self.logger.info("Password is entered: " + password)

	def click_loginbtn(self):
		self.driver.find_element(By.XPATH, cr.getElementLocators('Login', 'login_btn_xpath')).click()
		self.logger.info("Loggin button is clicked.")

	def login(self, username="", password=""):
		self.click_login_tab()
		self.enter_username(username)
		self.enter_password(password)
		time.sleep(1)
		self.click_loginbtn()
		time.sleep(5)

	def verifyLogin(self):
		try:
			self.driver.find_element(By.XPATH, cr.getElementLocators('Home', 'home'))
			return True
		except:
			return False

