import unittest
from Nov_3_1 import gfn

class NamesTestCase(unittest.TestCase):
    """测试Nov_3_1"""
    def test_first_last_name(self):
        fn=gfn('janis','joplin')
        self.assertEqual(fn,'Janis Joplin')

    def test_first_middle_last_name(self):
        fn=gfn('wolf','mozart','amadeus')
        self.assertEqual(fn,'Wolf Amadeus Mozart')

if __name__ =='__main__':
    unittest.main()

