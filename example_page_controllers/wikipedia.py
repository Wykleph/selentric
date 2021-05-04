from selenium.webdriver.remote.webdriver import WebDriver
from selentric import Page
from example_page_templates import wikipedia as wiki_templates


class WikipediaSearch(Page):  # Inherit from `Page`
    def __init__(self, driver: WebDriver):
        # Create a template that can evaluate the given conditions
        template: wiki_templates.WikipediaSearch = wiki_templates.WikipediaSearch(driver)

        self.search_url = 'https://en.wikipedia.org/w/index.php?search=&title=Special%3ASearch&go=Go'
        driver.get(self.search_url)
        # initialize the parent class and pass the template as input.
        super(WikipediaSearch, self).__init__(template, driver)

    def search(self, text: str):
        if self.search_url not in self.driver.current_url:
            self.driver.get(self.search_url)
        # Wait until the current web page matches the WikipediaSearch template
        # defined in example_page_templates folder.
        self.wait_for_match()
        self.wait_until_ready()  # Wait until the document.readyState == 'complete'

        # Use the search_input Locator to find the search_input
        # web element using selenium and send keystrokes.
        # Remember that you can treat the web element
        # as if they already exist.  You don't need to
        # call any functions to look anything up.
        self.search_input.clear()  # Make sure the search input box is empty
        self.search_input.send_keys(text)

        # Click the search button and wait for results to load.
        self.search_button.click()
        self.wait_until_ready()  # Wait for document ready state.
        self.wait_for_match()  # Wait until web page matches WikipediaSearch template.

        return self.search_results


class WikipediaSignIn(Page):
    def __init__(self, driver: WebDriver):
        # Use template created in example_page_templates folder.
        template: wiki_templates.WikipediaSignIn = wiki_templates.WikipediaSignIn(driver)
        # initialize the parent class and pass the template as input.
        super(WikipediaSignIn, self).__init__(template, driver)

    def sign_in(self, username: str, password: str, testing=False):
        self.driver.get('https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Special%3ASearch&returntoquery=search%3Dred%2Bpanda%26profile%3Dadvanced%26fulltext%3D1%26ns0%3D1')
        self.wait_until_ready()
        self.wait_for_match()
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        if not testing:
            self.login_button.click()
