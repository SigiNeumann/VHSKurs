import os 


 

from uebungen.basics import *
import unittest
import pytest

class DatatypesTest(unittest.TestCase):
    
    def test_addiere(self):
        self.assertEqual(5, addiere(2,3))
        self.assertEqual(-10, addiere(5,-15))
        self.assertEqual(5.3, addiere(5.0, 0.3))

    def test_halbiere(self):
        self.assertEqual(0, halbiere(0))
        self.assertEqual(-2, halbiere(-4))
        self.assertEqual(2.5, 5)

    def test_rest(self):
        pytest.raises( rest(2,0),ZeroDivisionError)
        self.assertEqual(rest(2,1),0)
        self.assertEqual(rest(7,4),3)

    def test_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(5.0), 5.0*(9/5)+32)
        self.assertEqual(celsius_to_fahrenheit(0.0), 32.0)
    
    def test_prozent(self):
        self.assertEqual(prozent(50.0,100.0),50.0)
        self.assertEqual(prozent(342.23, 232.0), (342.23/232.0) *100.0)

if __name__ == '__main__':
    
    unittest.main()