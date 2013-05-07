import selenium.webdriver
import selenium.common.exceptions
import selenium.webdriver.support.ui
import selenium.webdriver.support
import selenium.webdriver.support.expected_conditions
import selenium.webdriver.common.by
import selenium.common.exceptions
import appomatic_mapimport.mapimport
import logging
import contextlib

logger = logging.getLogger(__name__)

class SeleniumImport(appomatic_mapimport.mapimport.Import):

    def wait_for_xpath(self, xpath, negate=False):
        """Waits for an xpath to match the document, or of negate is True, to not match any longer."""
        cond = selenium.webdriver.support.expected_conditions.presence_of_element_located(
            (selenium.webdriver.common.by.By.XPATH,
             xpath))
        wait = selenium.webdriver.support.ui.WebDriverWait(self.connection, 10)
        try:
            if negate:
                logger.debug("Waiting for %s to go away" % xpath)
                return wait.until_not(cond)
            else:
                logger.debug("Waiting for %s" % xpath)
                return wait.until(cond)
        except selenium.common.exceptions.TimeoutException, e:
            self.connection.get_screenshot_as_file('timeout-screenshot.png')
            if negate:
                raise Exception("%s never went away" % xpath)
            else:
                raise Exception("%s never showed up" % xpath)

    @contextlib.contextmanager
    def connect(self):
        self.connection = selenium.webdriver.Firefox(
            firefox_profile=selenium.webdriver.firefox.firefox_profile.FirefoxProfile(
                profile_directory=self.FIREFOX_PROFILEDIR))
        yield
