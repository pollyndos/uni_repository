import unittest
import tokenizer
from tokenizer import Tokenizer


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
        self.assertEqual(tokenizer.stringdiv(s), ['я', 'иду', 'в', 'кино','cinema'])
      

    def test_empty_string(self):
        s = ''
        self.assertEqual(tokenizer.stringdiv(s), [])
     

    def test_no_spaces(self):
        s = 'яидувкиноcinema'
        self.assertEqual(tokenizer.stringdiv(s), ['яидувкиноcinema'])


    def test_digital_string(self):
        s = '012345'
        self.assertEqual(tokenizer.stringdiv(s), [])


    def test_first_nonalpha(self):
        s = '!!!!я иду в кино cinema '
        self.assertEqual(tokenizer.stringdiv(s), ['я', 'иду', 'в', 'кино','cinema'])
   

    def test_middle_nonapha(self):
        s = 'я иду в кино00000 111 00000cinema'
        self.assertEqual(tokenizer.stringdiv(s), ['я', 'иду', 'в', 'кино','cinema'])
    

    def test_last_nonalpha(self):
        s = 'я иду в кино cinema!!!! 000'
        self.assertEqual(tokenizer.stringdiv(s), ['я', 'иду', 'в', 'кино','cinema'])
        

if __name__ == '__main__':
    unittest.main()



