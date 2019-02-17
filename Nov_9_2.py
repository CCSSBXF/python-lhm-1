import unittest
from Nov_9_1 import Employee

class Test_Employee(unittest.TestCase):
    def setUp(self):
        self.test=Employee('asd','qwe',20000)

    def test_give_default_raise(self):
        self.test.give_raise(6000)
        self.assertEqual(self.test.money,26000)

    def test_give_custom_raise(self):
        name=self.test.first.title()+' '+self.test.last.title()
        self.assertEqual(name,'Asd Qwe')

if __name__=='__main__':
    unittest.main()
