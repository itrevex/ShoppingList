#test_shopping_list
"""
Class for unittesting ShoppingList Class;
Requirement for doing TDD
"""
import unittest
from ..app.shopping_list import ShoppingList, ItemNotInListException

class ShoppingListTest(unittest.TestCase):
    """
    Class for testing shopping list class
    """

    def setUp(self):
        """
        Setup instance for ShoppingList class from which to access class methods
        """
        self.shopping_list_1 = ShoppingList()
    
    def test_shopping_list_initial_total_amount(self):
        """ Test the name of the shopping list"""
        self.assertEqual(self.shopping_list_1.total_amount,0,msg='Shopping List Name Invalid')

    def test_shopping_list_initial_items(self):
        "Test to check whether dictionary of objects is empty at the start"
        self.assertFalse(self.shopping_list_1.items,msg="Invalid Size of Initial Items")

    def test_shopping_list_add_item(self):
        """Test adding item to shopping list"""
        self.shopping_list_1.add_item('pineapples',20,5)
        self.assertDictEqual(self.shopping_list_1.items, {'pineapples':[20,5]},msg='add_item method inaccurate')

    def test_shopping_list_remove_part_items(self):
        """ Test remove_item method"""
        self.shopping_list_1.add_item('apples',10,3)
        self.shopping_list_1.add_item('bananas',4,2)
        self.shopping_list_1.remove_item('apples',2)
        self.assertDictEqual(self.shopping_list_1.items,{'apples':[8,3],'bananas':[4,2]},msg='remove_item method inaccurate')
    
    def test_shopping_list_remove_all_items(self):
        """ Test remove_item method"""
        self.shopping_list_1.add_item('apples',10,3)
        self.shopping_list_1.add_item('bananas',4,2)
        self.shopping_list_1.remove_item('apples',10)
        self.assertDictEqual(self.shopping_list_1.items,{'bananas':[4,2]},msg='remove_item method inaccurate')

    def test_shopping_list_read_item(self):
        """Tests if return values for read item is correct"""
        self.shopping_list_1.add_item('oranges',10,3)
        oranges = self.shopping_list_1.read_item('oranges')
        self.assertListEqual(oranges,['oranges',10,30], msg='read_item method invalid')

    def test_shopping_list_total_amount_on_add_item(self):

        """ Test total amount in shopping list after adding items"""

        self.shopping_list_1.add_item('oranges',20,2)
        self.shopping_list_1.add_item('mangoes',5,1)
        self.assertEqual(self.shopping_list_1.total_amount,45,msg='Invalid Total Amount')

    def test_shopping_list_total_amount_on_remove_item(self):
        """ Test total amount in shopping list after removing items"""

        self.shopping_list_1.add_item('oranges',20,2)
        self.shopping_list_1.add_item('mangoes',5,1)
        self.shopping_list_1.remove_item('mangoes',4)
        self.assertEqual(self.shopping_list_1.total_amount,41,msg='Invalid Total Amount')

    def test_shopping_list_remove_item_expection(self):
        """
        Test to see if exception is raised if user tries to remove item from shopping list 
        that does not exist
        """
        with self.assertRaises(ItemNotInListException):
            self.shopping_list_1.remove_item('mangoes',10)

    def test_add_item_item_name_data_type(self):
        """
        tests if TypeError exception is raised if item_name is not str or is an 
        empty string on add_item
        """
        with self.assertRaises(TypeError):
            self.shopping_list_1.add_item(10,10,10)
    
    def test_add_item_number_of_items_data_type(self):
        """
        tests if TypeError exception is raised if number_of_items is not int
        or is zero on add_item
        """
        with self.assertRaises(TypeError):
            self.shopping_list_1.add_item('apples','brash',10)
    
    def test_add_item_item_amount_data_type(self):
        """
        tests if TypeError exception is raised if item_amount is not int
        or is zero on add_item
        """
        with self.assertRaises(TypeError):
            self.shopping_list_1.add_item('oranges',10,"")
    
    def test_remove_item_item_name_data_type(self):
        """
        tests if TypeError exception is raised if item_amount is not str
         or an empty str on remove_item
        """
        with self.assertRaises(TypeError):
            self.shopping_list_1.remove_item("",5)
    
    def test_read_item_item_name_data_type(self):
        """
        tests if TypeError exception is raised if item_name is not str
         or an empty str on remove_item
        """
        with self.assertRaises(TypeError):
            self.shopping_list_1.read_item(" ")

    
        

## raise exception if user tries to remove item that is not in list
## raise type error exception for all user input data


    
        
