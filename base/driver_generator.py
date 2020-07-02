from selenium import webdriver
from Utility import generate_logger as gl
from Utility import configreader as cr
from selenium.webdriver.chrome.options import Options


class DriverGenerator:
	logger = gl.custom_logger()

	def __init__(self, browser):
		# print("DriverGenerator call initiated")
		self.browser = browser

	def generateDriver(self):
		url = cr.configReader('Driver', 'URL')
		self.logger.info(url)

		if self.browser:
			if self.browser.lower() == "chrome":
				chrome_option = Options()
				chrome_option.add_argument("--headless")
				chrome_option.add_argument("--windows-size=1920*1080")
				# driverLocation = cr.configReader('Driver', 'Location')
				# driver = webdriver.Chrome(executable_path=driverLocation, chrome_options=chrome_option)
				driver = webdriver.Chrome()
				driver.implicitly_wait(3)
				driver.maximize_window()
				driver.get(url)
				self.logger.info("Driver Initiated and webPage Launched..")
				return driver
			else:
				self.logger.error("Can run on chrome browser only.")
		else:
			self.logger.error("Can run on chrome browser only. add '--browser chrome' argument")
