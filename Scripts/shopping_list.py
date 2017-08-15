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
        
        Method updates total_amount and items
        """

        self.items[item_name] = [number_of_items,cost_per_item]
        self.total_amount += number_of_items*cost_per_item
    
    def remove_item(self,item_name):
        """
        Remove item from shopping list
        remove item `item_name` from the items __dict__
        updates the total_amount
        """
        
        self.total_amount -= self.items[item_name][0]*self.items[item_name][1]
        self.items.pop(item_name,None)
        
    def read_item(self,item_name):
        """
        Read out item from dictionary
        returns item with values from dictionary
        Amount is returned is returned as a total of all objects per item
        """
        number_of_items = self.items[item_name][0]
        return [item_name,number_of_items,number_of_items*self.items[item_name][1]]