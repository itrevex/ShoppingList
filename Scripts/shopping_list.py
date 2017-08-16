#shopping_list
"""
Class used for creating shopping list. User can add item name, number of items
and cost of each item
"""

class ItemNotInListException(Exception):
    """
    Exception class if one tries to remove item not in shopping list from 
    shopping list
    """
    pass

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

        if not isinstance(item_name, str) or not item_name:
            raise TypeError("Item Name Should Be A Word")
        
        if not item_name.strip():
            raise TypeError("Item Name Should Be A Word")
        
        if not isinstance(number_of_items,int) or number_of_items == 0:
            raise TypeError("Number of Items should be Counting Number > 0")
        
        if not isinstance(cost_per_item,int) or cost_per_item == 0:
            raise TypeError("Cost Of Item Should Be Counting Number Greater Than Zero")
        

        self.items[item_name] = [number_of_items,cost_per_item]
        self.total_amount += number_of_items*cost_per_item
    
    def remove_item(self,item_name,number_items_on_item):
        """
        Remove item from shopping list
        remove item `item_name` from the items __dict__
        updates the total_amount
        remove the number_items_on_item specified from the total items pool
        """
        if not isinstance(item_name, str) or not item_name:
            raise TypeError("Item Name Should Be A Word")
        
        if not item_name.strip():
            raise TypeError("Item Name Should Be A Word")

        if item_name not in self.items:
            raise ItemNotInListException('Item You Are Trying To Remove Is Not In Shopping List')
        
        self.total_amount -= self.items[item_name][1]*number_items_on_item
        if number_items_on_item >= self.items[item_name][0]:
            self.items.pop(item_name,None)
        else:
            left_items = self.items[item_name][0] - number_items_on_item
            cost_of_item = self.items[item_name][1]
            self.items[item_name] = [left_items,cost_of_item]
        
    def read_item(self,item_name):
        
        """
        Read out item from dictionary
        returns item with values from dictionary
        Amount is returned is returned as a total of all objects per item
        """
        
        if not isinstance(item_name, str) or not item_name:
            raise TypeError("Item Name Should Be A Word")
        
        if not item_name.strip():
            raise TypeError("Item Name Should Be A Word")

    
        number_of_items = self.items[item_name][0]
        return [item_name,number_of_items,number_of_items*self.items[item_name][1]]