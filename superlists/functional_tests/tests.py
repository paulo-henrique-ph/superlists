from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_for_one_user(self):
        # Open the Web Browser
        self.browser.get(self.live_server_url)

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


        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # Add another task "Use peacock feathers to make a fly"
        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys("Use peacock feathers to make a fly")
        input_box.send_keys(Keys.ENTER)



        # Show the two items in the list
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table(
            "2: Use peacock feathers to make a fly"
        )

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys("Buy peacock feathers")
        input_box.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # Check if user has unique url
        user_list_url = self.browser.current_url
        self.assertRegex(user_list_url, r'/lists/(\d+)/')

        self.browser.quit()

        # Other user starts the website
        self.browser = webdriver.Chrome()

        # No sign of other user list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertNotIn("make a fly", page_text)

        # Add new item to the list
        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys("Buy milk")
        input_box.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy milk")

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # Input box is in the center
        input_box = self.browser.find_element_by_id("id_new_item")
        self.assertAlmostEqual(
            input_box.location["x"] + input_box.size["width"] / 2,
            512,
            delta=10
        )
