from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Cannot accept empty strings
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector(
                ".has-error"
            ).text,
            "You can't have an empty list item"
        ))

        # Try again with a valid element
        self.get_item_input_box().send_keys("Buy milk")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy milk")

        # Try again empty strings
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector(
                ".has-error"
            ).text,
            "You can't have an empty list item"
        ))

        # Try once more with a valid element
        self.get_item_input_box().send_keys("Buy tea")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy milk")
        self.check_for_row_in_list_table("2: Buy tea")
