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

        if not self.validate_email():
            raise InValidEmailExcpetion('User Email Invalid')

        if not self.validate_password():
            raise InValidPasswordExcpetion('Password must be atleast six \'6\' characters long')

        email_password = self.email,self.password
        return email_password in self.online_data

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