from msilib.schema import SelfReg
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def get_error_element(self):
        return self.browser.find_element_by_css_selector(".has-error")

    def test_cannot_add_empty_list_items(self):
        # Cannot accept empty strings
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector("#id_text:invalid")
        )

        # Try again with a valid element
        self.get_item_input_box().send_keys("Buy milk")
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector("#id_text:valid")
        )
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy milk")

        # Try again empty strings
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy milk")
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector("#id_text:invalid")
        )

        # Try once more with a valid element
        self.get_item_input_box().send_keys("Buy tea")
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector("#id_text:valid")
        )
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy milk")
        self.check_for_row_in_list_table("2: Buy tea")

    def test_cannot_add_duplicate_items(self):
        # Goes to homepage and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys("Buy wellies")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy wellies")

        # Tries to insert a duplicate item
        self.get_item_input_box().send_keys("Buy wellies")
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Sees a helpfull error message
        self.wait_for(
            lambda: self.assertEqual(
                self.get_error_element().text,
                "You've already got this item in your list",
            )
        )

    def test_error_messages_are_cleared_on_input(self):
        # Start a new list and causes a validation error
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys("Banter too thick")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Banter too thick")
        self.get_item_input_box().send_keys("Banter too thick")
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(
            lambda: self.assertTrue(
                self.get_error_element().is_displayed()
            )
        )

        # Starts to type on the input box to clear the error
        self.get_item_input_box().send_keys("a")

        self.wait_for(
            lambda: self.assertFalse(
                self.get_error_element().is_displayed()
            )
        )
