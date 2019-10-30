import unittest
import func

class TestStringMethods(unittest.TestCase):

    def test_first_alpha(self):
        s = 'я иду в кино cinema '
        self.assertEqual(func.stringdiv(s), ['я', 'иду', 'в', 'кино','cinema'])
        self.assertEqual(len(func.stringdiv(s)), 5)

    def test_empty_string(self):
        s = ''
        self.assertEqual(func.stringdiv(s), [])
        self.assertEqual(len(func.stringdiv(s)), 0)

    def test_no_spaces(self):
        s = 'яидувкиноcinema'
        self.assertEqual(func.stringdiv(s), ['яидувкиноcinema'])
        self.assertEqual(len(func.stringdiv(s)), 1)

    def test_digital_string(self):
        s = '012345'
        self.assertEqual(func.stringdiv(s), [])
        self.assertEqual(len(func.stringdiv(s)), 0)

    def test_first_nonalpha(self):
        s = '!!!!я иду в кино cinema '
        self.assertEqual(func.stringdiv(s), ['я', 'иду', 'в', 'кино','cinema'])
        self.assertEqual(len(func.stringdiv(s)), 5)

    def test_middle_nonapha(self):
        s = 'я иду в кино00000 111 00000cinema'
        self.assertEqual(func.stringdiv(s), ['я', 'иду', 'в', 'кино','cinema'])
        self.assertEqual(len(func.stringdiv(s)), 5)

    def test_last_nonalpha(self):
        s = 'я иду в кино cinema!!!! 000'
        self.assertEqual(func.stringdiv(s), ['я', 'иду', 'в', 'кино','cinema'])
        self.assertEqual(len(func.stringdiv(s)), 5)

    

if __name__ == '__main__':
    unittest.main()
