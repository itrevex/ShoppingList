import unittest
from login import LogIn, InValidEmailExcpetion, InValidPasswordExcpetion
"""
Unittest class for testing login class instance
"""

class LoginTest(unittest.TestCase):
    
    """
    Class for running login tests
    """

    def setUp(self):
        self.isaac_ssekamattte = LogIn("isaac@isaac.com","123456i")
        self.steve = LogIn("steve@steve.com","qwerty")
    
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

    def test_server_sent_email(self):
        """
        test constant email kept in tupple mimicing server sent login email
        """
        email = "steve@steve.com"
        self.assertEqual(self.isaac_ssekamattte.online_data[0],email,msg="Incorrect Value for Email in Tupple")
       
    def test_server_sent_password(self):
        """
        test constant email kept in tupple mimicing server sent login email
        """
        local_email_password = ("steve@steve.com","qwerty")
        server_email_password = self.isaac_ssekamattte.online_data.pop(0)
        self.assertEqual(local_email_password,server_email_password,
        msg="Incorrect Value for password in Tupple")

    #change of logic, first comment this block this out
    """"
    def test_check_email(self):
        """
        Test method for comparing emails
        """
        self.assertTrue(self.steve.checkemail(self.steve.email),msg="Check Email Method Inaccurate")

    def test_check_password(self):
        """
        Test method for comparing passwords
        """
        self.assertTrue(self.steve.checkpasword(self.steve.password),msg="Check Email Method Inaccurate")
    """"
    def test_check_login(self):
        """
        Test method for login on success
        """
        self.assertTrue(self.steve.login(self.steve.email,self.steve.password),
        msg="Check Email Method Inaccurate")

    def test_password_validity(self):
        """
        tests if InValidPassWordException exception is raised if password is less 
        than six characters long
        """
        with self.assertRaises(InValidPasswordExcpetion):
            self.isaac_ssekamattte.password(8)

    def test_email_validity(self):
        """
        tests if InValidPassWordException exception is raised if email is
        string with @ and a `.` in it >= 4 characters
        """
        with self.assertRaises(InValidEmailExcpetion):
            self.isaac_ssekamattte.password('dsdsaasd8')
