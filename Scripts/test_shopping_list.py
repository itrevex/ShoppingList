"""
Class for unittesting ShoppingList Class;
Requirement for doing TDD
"""
import unittest
import pytest

from shopping_list import ShoppingList

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
        self.assertEqual(self.shopping_list_1.total_amount,0,"Shopping List Name Invalid")

    def test_shopping_list_total_amount(self):

        """ Test total amount in shopping list after adding items"""

        self.shopping_list_1.add_item('oranges',20,2)
        self.shopping_list_1.add_item('mangoes',5,1)

        self.assertEqual(self.shopping_list_1.total_amount,45,'Invalid Total Amount')



    
        
