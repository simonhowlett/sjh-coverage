import unittest

def IsOdd(n):
    return n % 2 == 1

def IsEven(x):
    return x % 2 == 0

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testtwo(self):
        self.failIf(IsOdd(2))
'''
class IsEvenTests(unittest.TestCase):

    def testthree(self):
        self.failUnless(IsEven(2))

    def testfour(self):
        self.failIf(IsEven(1))
'''

