from selenium import webdriver
from page import HomePage
from page import AboutPage
from locator import CommonPageLocators
from locator import AboutPageLocators


class TestPyOrgBase(unittest.TestCase):
    def setUp(self):
        opts = webdriver.FirefoxOptions()
        opts.set_headless()
        self.driver = webdriver.Remote(command_executor='http://192.168.3.216:4444/wd/hub',
                                       desired_capabilities=chrome_options.to_capabilities())

    def tearDown(self):
        self.driver.quit()
        self.driver.stop_client()


class TestHome(TestPyOrgBase):
    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)

    def test_TC001_py3_doc_button(self):
        self.home.hover_to(CommonPageLocators.DOC)
        self.home.assert_elem_text(CommonPageLocators.PY3_DOC_BUTTON, 'Python 3.x Docs')
        self.home.click(CommonPageLocators.PY3_DOC_BUTTON)
        assert self.driver.current_url == 'https://docs.python.org/3/'

    # skip etmek için unittest.skip kullanııyor. içinde de mesaj var. istediğimizi yazabiliriz. "melis" yazarsak "melis" çıkar gibi.
    # testi neden skip ettiğimizi hatırlamak için bu mesajı yazarız.
    @unittest.skip('skipping example for decarator')
    def test_TC002_blahblah_search(self):
        self.home.search_for('blahblah')
        self.home.assert_elem_text(CommonPageLocators.SEARCH_RESULT_LIST, 'No results found.')

    # with unit test. unittestin sağladığı bir koddur bu.
    def test_TC004_assert_title(self):
        self.assertEqual(self.home.driver.title, "Welcome to Python.org")


class TestAbout(TestPyOrgBase):
    def setUp(self):
        super().setUp()
        self.about = AboutPage(self.driver)

    def test_TC003_upcoming_events_check(self):
        self.about.assert_elem_text(AboutPageLocators.UPCOMING_EVENTS, 'Upcoming Events')

    # with unit test. current url'de about var mı diye bakıoruz. about page'te.
    def test_TC005_assert_url(self):
        self.assertTrue('about' in self.about.driver.current_url)


if __name__ == '__main__':
    unittest.main()
