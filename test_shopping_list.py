import unittest
from shopping_list import ShoppingList

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({'牙刷':5, '沐浴露':15, '电池':20})
    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 40)


if __name__ == '__main__':
    unittest.main()
