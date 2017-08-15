#shopping_list
"""
Class used for creating shopping list. User can add item name, number of items
and cost of each item
"""

class ShoppingList():
    """
    Shopping list class will have the methods to call on each shopping list instance
    """
    def __init__(self):
        self.total_amount = 0
        self.items = {}
    
    def add_item(self,item_name, number_of_items,cost_per_item):
        """ 
        Add item to shopping list
        item_name  is the name of the item you wnat to to shopping list
        number_of_items defines how many items you want to add
        cost_per_item defines the unit cost of an item
        """
        pass