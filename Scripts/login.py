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
        self.online_data = 'steve@steve.com','qwerty'
    
    
    def check_email(self):
        """
        Checks if email matches any emails from server
        """
        return self.email == self.online_data[0]

    def check_password(self):
        """
        checks if password matches passwords on
        """
        return self.password == self.online_data[1]
