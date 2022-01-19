import unittest
import triangle

class Test(unittest.TestCase):
    def CheckEqual(self):
        ##Arrange
        one = (2)
        two = (5)
        three = (5)
        ##Act
        receive = triangle.triangleCheck(one,two,three)
        ##Assert
        self.assertEqual('equilateral', receive) 

if __name__ == '__main__':
    unittest.main()