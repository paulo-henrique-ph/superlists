from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        # Cannot accept empty strings
        self.fail("Write me")
