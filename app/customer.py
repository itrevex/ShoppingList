#login.py
"""
Login class for housing login methods
"""
class InValidEmailExcpetion(Exception):
    """
    Email exception class
    """
    pass

class InValidPasswordExcpetion(Exception):
    """
    password exception class
    """
    pass

class Customer():
    """
    Shopping List login class
    Created on 16/08/2017 by Isaac Ssekamatte
    """
    def __init__(self,email,password):
            
        self.email = email
        self.password = password
        self.online_data = {("steve@steve.com","qwerty"),("isaac@isaac.com","123456i")}
        self.login_status = False
        self.shopping_lists = {}
            
    def login(self):
        
        """
        checks if password and email match server values
        Allows or declines user to access page
        """

        if not self.validate_email():
            raise InValidEmailExcpetion('User Email Invalid')

        if not self.validate_password():
            raise InValidPasswordExcpetion('Password must be atleast six \'6\' characters long')

        email_password = self.email,self.password
        self.login_status = email_password in self.online_data

    def validate_email(self):
        """
        Method to validate user email. Email should at least an '@','.' character
        and also be greater 4 characters long
        """
        email = str(self.email)
        return '@' in email and '.' in email and len(email) > 4

    def validate_password(self):
        """
        Method to validate user password. Password should be atleast 6 characters long
        """
        password = str(self.password)
        return len(password) >= 6

    def create_shopping_list(self, name_shopping_list,shopping_list):
        """
        creates shopping list using from items list passed in and 
        the shopping list name
        """
        self.shopping_lists[str(name_shopping_list)] = shopping_list

    def remove_shopping_list(self,name_shopping_list):
        """
        removes shopping list from collection of shopping lists
        """
        self.shopping_lists.pop(name_shopping_list, None)

    def update_shopping_list(self,name_shopping_list,update_list):
        """
        updates shopping list in pool of shopping lists
        """
        self.shopping_lists[name_shopping_list] = update_list

    def show_items_in_shopping_list(self,name_shopping_list):
        """
        returns list of values of shopping list to display
        """

        return [name_shopping_list,self.shopping_lists[name_shopping_list]]

    def logout(self):
        """
        changes customer login status
        """
        self.login_status = False