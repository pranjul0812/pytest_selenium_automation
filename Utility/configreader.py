import configparser
import os


def configReader(section, key):
	config = configparser.ConfigParser()
	dirname = os.path.abspath('.')
	filename = dirname + '/ConfigFiles/config.cfg'
	config.read(filename)
	return config.get(section, key)


def getElementLocators(section, key):
	config = configparser.ConfigParser()
	dirname = os.path.abspath('.')
	filename = dirname + '/ConfigFiles/Elements.cfg'
	config.read(filename)
	return config.get(section, key)

# location = configReader('Driver', 'Location')
# location = getElementLocators('Home', 'home')
# print(location)
# url = configReader('Driver', 'URL')
# print(location, url)
# driverLocation = "D:/Tools/Selenium/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driverLocation)
# driver.maximize_window()
# driver.get(url)


