
"""
Unittest class for testing management class
"""

import unittest
from ..app.management import Management, InValidEmailExcpetion, InValidPasswordExcpetion

class ManagementTest(unittest.TestCase):
    
    def setUp(self):
        """Instantiate Management Class"""
        self.management = Management()
    
    def test_start_number_of_customers(self):
        """Test Starting Number of Customers"""

        self.assertFalse(self.management.customers,msg="Starting Number of Customers Wrong")
    
    def test_add_customer(self):
        """test add_customer_method"""

        customer=Customer("email","password")
        self.management.add_customer(customer)
        self.assertEqual(self.management.customers[0],customer,msg="add_customer Method Invalid")
    
    def test_remove_customer(self):
        """Test remove_customer method"""
        customer=Customer("email","password")
        self.management.add_customer(customer)
        self.management.remove_customer(customer)
        self.assertEqual(self.management.customers,[],msg="remove_customer Method Invalid")
