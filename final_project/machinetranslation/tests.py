# unit test case
import unittest
from translator import english_to_french, french_to_english
  
class TestStringMethods(unittest.TestCase):
    def test_english_to_french(self):
        message = "Should be null"
        # assertNull
        self.assertNull(english_to_french(''), '', message)
        self.assertEquals(english_to_french('Hello'), 'Bonjour', message)
    
    def test_french_to_english(self):
        message = "Should be null"
        # assertNull
        self.assertNull(french_to_english(''), '', message)
        self.assertEquals(french_to_english('Bonjour'), 'Hello', message)
  
if __name__ == '__main__':
    unittest.main()