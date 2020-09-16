import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Open the Web Browser
        self.browser.get("http://localhost:8000")

        # See if the title mentions todo list
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test")

        # Insert a task "Buy peacock feathers"

        # When inserted show the item "1: Buy peacock feathers"

        # Add another task "Use peacock feathers to make a fly"

        # Show the two items in the list

        # Generate a unique url for the user

        # Access this unique url and see if the tasks still included
