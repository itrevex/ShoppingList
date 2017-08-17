
"""
Unittest class for testing login class instance
"""

import unittest
from customer import Customer, InValidEmailExcpetion, InValidPasswordExcpetion

class LoginTest(unittest.TestCase):
    
    """
    Class for running login tests
    """

    def setUp(self):
        self.isaac_ssekamattte = Customer("isaac@isaac.com","123456i")
        self.steve = Customer("steve@steve.com","qwerty")
        self.invalid_email= Customer("6rrrrer","123421")
        self.invalid_password= Customer("steve@steve.com","133")
    
    def test_shopping_lists_init_value(self):
        """tests if shopping list starts empty"""
        self.assertEqual(self.steve.shopping_lists, {},msg={"New Customer Shopping List Not Empty"})
    
    def test_login_status_init(self):
        """tests if customer starts loged out"""
        self.assertFalse(self.steve.login_status,msg="Customer Logged In before SignIn")
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

    def test_customer_email_password_pairs(self):
        """
        test constant email kept in tupple mimicing server sent login email
        """
        server_data = {("steve@steve.com","qwerty"),("isaac@isaac.com","123456i")}
        self.assertEqual(self.isaac_ssekamattte.online_data,server_data,msg="Incorrect Value for Email in Tupple")
       

    def test_check_login(self):
        """
        Test method for login on success
        """
        self.steve.login()
        self.assertTrue(self.steve.login_status,msg="Check Email Method Inaccurate")
    
    def test_log_out(self):
        """ Test Customer Log Out"""
        self.steve.logout()
        self.assertFalse(self.steve.login_status,msg="Log out Method Incacurate")

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

    def test_create_shopping_list(self):
        """Check validity of create shopping list method"""
        shopping_list = {"oranges":[5,200],"mangoes":[6,1000]}
        self.steve.create_shopping_list("grosseries",shopping_list)
        self.assertEqual(self.steve.shopping_lists['grosseries'],
        shopping_list,msg="Create Shopping List Method Inaccurate")

    def test_remove_shopping_list(self):
        """Checks if remove_shopping_list() method is function well"""
        grosseries = {"oranges":[5,200],"mangoes":[6,1000]}
        toilatories = {"bathing_soap":[1,5000],"toothpaster":[2,4500],"vaseline":[1,2500]}
        self.steve.create_shopping_list("grosseries",grosseries)
        self.steve.create_shopping_list("toilatories",toilatories)
        self.steve.remove_shopping_list("grosseries")
        shopping_lists = {"toilatories":toilatories}
        self.assertEqual(self.steve.shopping_lists,shopping_lists,
        msg="remove_shopping_list Method Inaccurate")


    def test_update_shopping_list(self):
        """tests if update shopping_list Method is accurate"""
        grosseries = {"oranges":[5,200],"mangoes":[6,1000]}
        self.steve.create_shopping_list("grosseries",grosseries)
        updated_grosseries = {"oranges":[5,200],"mangoes":[6,1000],"pees":[5,4000]}
        self.steve.update_shopping_list("grosseries",updated_grosseries)
        self.assertEqual(self.steve.shopping_lists["grosseries"],updated_grosseries,
        msg="update_shopping_list_method_inaccurate")

    def test_show_shopping_list_item(self):
        """tests show items feature on customer object"""
        grosseries = {"oranges":[5,200],"mangoes":[6,1000]}
        self.steve.create_shopping_list("grosseries",grosseries)
        grosseries_list = ["grosseries",grosseries]
        self.assertEqual(self.steve.show_shopping_list("grosseries"),grosseries_list,
        msg="show_grosseries() Method Inaccurate")

        
    