from bannedWordChecker import *
from bannedwords import bannedwords
import unittest


class WordReturns(unittest.TestCase):
    
    def test_bannedWordReturnsTrue(self):

        for word in bannedwords:
            firstWord = word
            secWord = 'good'
            result = hasBannedWords(firstWord,secWord)
            self.assertTrue(result, word + ' was not banned')
    
    def test_allowedWordsReturnFalse(self):

        firstWord = 'nice'
        secWord = 'good'
        result = hasBannedWords(firstWord,secWord)
        self.assertFalse(result,'Allowed words returned as banned')

    def test_oneBannedWordReturnsTrue(self):
        firstWord = 'shit'
        secWord = 'happy'
        result = hasBannedWords(firstWord,secWord)
        self.assertTrue(result)

    def test_upperCaseBannedWordsReturnsTrue(self):
        
        firstWord = 'Shit'
        secWord = 'Good'
        result = hasBannedWords(firstWord,secWord)
        self.assertTrue(result)



if __name__ == "__main__":
    unittest.main()