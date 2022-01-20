import unittest
import triangle

class Test(unittest.TestCase):
    
    def testcheckEqual(self):
        ##Arrange
        one = (5)
        two = (5)
        three = (5)
        ##Act
        receive = triangle.TriangleCheck( one, two , three )
        ##Assert
        self.assertEqual('equilateral', receive) 

    def testcheckFirstIsosceles(self):
        ##Arrange
        one = (3)
        two = (5)
        three = (5)
        ##Act
        receive = triangle.TriangleCheck( one, two , three )
        ##Assert
        self.assertEqual('isosceles', receive) 

    def testcheckSecondIsosceles(self):
        ##Arrange
        one = (5)
        two = (3)
        three = (5)
        ##Act
        receive = triangle.TriangleCheck( one, two , three )
        ##Assert
        self.assertEqual('isosceles', receive) 

    def testcheckThirdIsosceles(self):
        ##Arrange
        one = (5)
        two = (5)
        three = (3)
        ##Act
        receive = triangle.TriangleCheck( one, two , three )
        ##Assert
        self.assertEqual('isosceles', receive) 

    def testcheckIrregular(self):
        ##Arrange
        one = (1)
        two = (2)
        three = (3)
        ##Act
        receive = triangle.TriangleCheck( one, two , three )
        ##Assert
        self.assertEqual('irregular', receive) 
    

    
if __name__ == '__main__':
    unittest.main()