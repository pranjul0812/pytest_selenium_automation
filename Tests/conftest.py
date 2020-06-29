import pytest
from EndToEndAutomation.base.driver_generator import DriverGenerator


@pytest.fixture(scope='class')
def oneTimeSetUp(request, browser):
	dg = DriverGenerator(browser)
	driver = dg.generateDriver()
	if request.cls is not None:
		request.cls.driver = driver
	yield driver
	driver.close()


def pytest_addoption(parser):
	parser.addoption("--browser")


@pytest.fixture(scope='session')
def browser(request):
	return request.config.getoption("--browser")