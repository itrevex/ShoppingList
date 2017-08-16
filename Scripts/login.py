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

class LogIn():
    """
    Shopping List login class
    Created on 16/08/2017 by Isaac Ssekamatte
    """
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.online_data = {("steve@steve.com","qwerty"),("isaac@isaac.com","123456i")}
            
    def login(self):
        """
        checks if password and email match server values
        Allows or declines user to access page
        """
        email_password = self.email,self.password
        return email_password in self.online_data

