import unittest
import time
from RData import RDataStore

ds = RDataStore()
class Tester(unittest.TestCase):
    def test_all(self):
        # Test Case 1: Not a JSON value
        self.assertEqual(ds.create(1, '{ 4', 0), "VALUE_ERROR: Not a valid value. Value should be in JSON format")
        self.assertEqual(ds.create(1, "3 } ", 2), "VALUE_ERROR: Not a valid value. Value should be in JSON format")

        # Test Case 2: Correct creation
        self.assertEqual(ds.create(1, "4", 0), "Key sucessfully created")
        self.assertEqual(ds.create(5, 3, 0), "Key sucessfully created")

        # Test Case 3: Insertion of already inserted key
        self.assertEqual(ds.create(1, 54, 0), "KEY_ERROR: Key already exists")
        self.assertEqual(ds.create(5, '{"firstName":"John", "lastName":"Doe"}', 4), "KEY_ERROR: Key already exists")
        
        # Test Case 4: Key capping to 32 chars
        self.assertEqual(ds.create("This is a very long key, it must be longer 32 chars", 54, 200), "Key sucessfully created")
        self.assertEqual(ds.read("This is a very long key, it must"), "54")

        # Test Case 5: Reading / Deleting a key who's TTL has expired
        self.assertEqual(ds.create(7, 8429, 5), "Key sucessfully created")
        print("Waiting for TTL to expire...")
        time.sleep(10)
        self.assertEqual(ds.read(5), "TTL_ERROR: You cannot read after Time-To-Live")
        self.assertEqual(ds.delete(5), "TTL_ERROR: You cannot delete after Time-To-Live")
        
        # Test Case 6: Deleting a key
        self.assertEqual(ds.create(8, 4244, 5), "Key sucessfully created")
        self.assertEqual(ds.delete(8), "Key successfully deleted")