from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # Input box is in the center
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location["x"] + input_box.size["width"] / 2, 512, delta=10
        )

        # Start a new list and the items still centered
        input_box.send_keys("testing")
        input_box.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: testing")

        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location["x"] + input_box.size["width"] / 2, 512, delta=10
        )
