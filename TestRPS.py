import unittest
import unittest.mock as mock
import RPS

'''Made by Topi Aila'''

class TestRPS(unittest.TestCase):

    def testUserWin(self):
        ##Arrange
        bot = 'rock'
        user = 'paper'
        expected_Value = "User wins"
        ##Act
        with mock.patch.object(RPS, 'input', return_value=user):
            result_value = RPS.RockPaperScissors(bot)
            ##Assert
            self.assertEqual(expected_Value, result_value)
    
    def testBotWin(self):
        ##Arrange
        bot = 'paper'
        user = 'rock'
        expected_Value = "Computer wins"
        ##Act
        with mock.patch.object(RPS, 'input', return_value=user):
            result_value = RPS.RockPaperScissors(bot)
            ##Assert
            self.assertEqual(expected_Value, result_value)

    def testTie(self):
        ##Arrange
        bot = 'scissors'
        user = 'scissors'
        expected_Value = "Draw"
        ##Act
        with mock.patch.object(RPS, 'input', return_value=user):
            result_value = RPS.RockPaperScissors(bot)
            ##Assert
            self.assertEqual(expected_Value, result_value)
    
    def testFail(self):
        ##Arrange
        bot = 'rock'
        user = 'UserMissSpell'
        expected_Value = 'Fail'
        ##Act
        with mock.patch.object(RPS, 'input', return_value=user):
            result_value = RPS.RockPaperScissors(bot)
            ##Assert
            self.assertEqual(expected_Value, result_value)

if __name__ == '__main__':
    unittest.main()