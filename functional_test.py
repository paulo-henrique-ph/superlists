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

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])

        # Add another task "Use peacock feathers to make a fly"
        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys("Use peacock feathers to make a fly")
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)


        # Show the two items in the list
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
        self.assertIn(
            "2: Use peacock feathers to make a fly",
            [row.text for row in rows]
        )

        # Generate a unique url for the user
        self.fail("Finish the test")

        # Access this unique url and see if the tasks still included


if __name__ == "__main__":
    unittest.main(warnings="ignore")
