import unittest
from tokenizer import Tokenizer
import func

class TestTokenizer(unittest.TestCase):

    def setUp(self):
        self.t = Tokenizer()


    def test_first_alpha(self):
        s = 'я иду в кино cinema '
        self.assertEqual(self.t.tokenize(s), ['я', 'иду', 'в', 'кино','cinema'])
     

    def test_empty_string(self):
        s = ''
        self.assertEqual(self.t.tokenize(s), [])
      

    def test_no_spaces(self):
        s = 'яидувкиноcinema'
        self.assertEqual(self.t.tokenize(s), ['яидувкиноcinema'])
       

    def test_digital_string(self):
        s = '012345'
        self.assertEqual(self.t.tokenize(s), [])
       

    def test_first_nonalpha(self):
        s = '!!!!я иду в кино cinema '
        self.assertEqual(self.t.tokenize(s), ['я', 'иду', 'в', 'кино','cinema'])
       

    def test_middle_nonapha(self):
        s = 'я иду в кино00000 111 00000cinema'
        self.assertEqual(self.t.tokenize(s), ['я', 'иду', 'в', 'кино','cinema'])
      

    def test_last_nonalpha(self):
        s = 'я иду в кино cinema!!!! 000'
        self.assertEqual(self.t.tokenize(s), ['я', 'иду', 'в', 'кино','cinema'])
    
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



