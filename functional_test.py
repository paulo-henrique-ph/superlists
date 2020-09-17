import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)


        # See if there is an input box
        input_box = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            input_box.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        # Insert a task "Buy peacock feathers"
        input_box.send_keys("Buy peacock feathers")

        # When inserted show the item "1: Buy peacock feathers"
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_elements_by_id("id_list_table")
        rows = table.find_element_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows)
        )

        # Add another task "Use peacock feathers to make a fly"
        self.fail("Finish the test")

        # Show the two items in the list

        # Generate a unique url for the user

        # Access this unique url and see if the tasks still included


if __name__ == "__main__":
    unittest.main(warnings="ignore")
