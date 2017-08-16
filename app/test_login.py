
"""
Unittest class for testing login class instance
"""

import unittest
from login import LogIn, InValidEmailExcpetion, InValidPasswordExcpetion

class LoginTest(unittest.TestCase):
    
    """
    Class for running login tests
    """

    def setUp(self):
        self.isaac_ssekamattte = LogIn("isaac@isaac.com","123456i")
        self.steve = LogIn("steve@steve.com","qwerty")
        self.invalid_email= LogIn("6rrrrer","123421")
        self.invalid_password= LogIn("steve@steve.com","133")
    
    def test_constructor_email(self):
        """
        Test initial string passed in as email to Login Constructor
        """
        self.assertEqual(self.isaac_ssekamattte.email,"isaac@isaac.com","__init__ method inaccurate")

    def test_constructor_password(self):
        """
        Test initial string passed in as password to Login Constructor
        """
        self.assertEqual(self.isaac_ssekamattte.password,"123456i","__init__ method inaccurate")

    def test_server_sent_email_password_pairs(self):
        """
        test constant email kept in tupple mimicing server sent login email
        """
        server_data = {("steve@steve.com","qwerty"),("isaac@isaac.com","123456i")}
        self.assertEqual(self.isaac_ssekamattte.online_data,server_data,msg="Incorrect Value for Email in Tupple")
       

    def test_check_login(self):
        """
        Test method for login on success
        """
        self.assertTrue(self.steve.login(),msg="Check Email Method Inaccurate")

    def test_password_validity(self):
        """
        tests if InValidPassWordException exception is raised if password is less 
        than six characters long
        """
        with self.assertRaises(InValidPasswordExcpetion):
            self.invalid_password.login()

    def test_email_validity(self):
        """
        tests if InValidPassWordException exception is raised if email is
        string with @ and a `.` in it >= 4 characters
        """
        with self.assertRaises(InValidEmailExcpetion):
           self.invalid_email.login()
