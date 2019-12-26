import unittest
import tokenizer
from tokenizer import Tokenizer
from tokenizer import Token


class TestTokenizerWithCategories(unittest.TestCase):  # class Tokenizer, method tokenize_categories

    def setUp(self):
        self.t = Tokenizer()

    def test_first_alpha(self):
        s = self.t.tokenize_categories('я иду в кино')
        self.assertEqual(s[0], Token("я", "alpha", 0, 1))
        self.assertEqual(len(s), 7)

    def test_empty_string(self):
        s = self.t.tokenize_categories('')
        self.assertEqual(len(s), 0)
        self.assertEqual(s, [])

    def test_no_spaces(self):
        s = self.t.tokenize_categories('яидувкиноcinema')
        self.assertEqual(s, [Token('яидувкиноcinema', 'alpha', 0, 15)])
        self.assertEqual(len(s), 1)

    def test_digital_string(self):
        s = self.t.tokenize_categories('012345')
        self.assertEqual(len(s), 1)
        self.assertEqual(s, [Token('012345', 'digit', 0, 6)])

    def test_first_nonalpha(self):
        s = self.t.tokenize_categories('!!!!я иду в кино cinema')
        self.assertEqual(len(s), 10)
        self.assertEqual(s[0], Token('!!!!', 'punct', 0, 4))

    def test_middle_nonapha(self):
        s = self.t.tokenize_categories('я иду в кино00000 111 00000cinema')
        self.assertEqual(len(s), 13)
        self.assertEqual(s[7], Token('00000', 'digit', 12, 17))
        self.assertEqual(s[9], Token('111', 'digit', 18, 21))

    def test_last_nonalpha(self):
        s = self.t.tokenize_categories('я иду в кино cinema!!!! 000')
        self.assertEqual(len(s), 12)
        self.assertEqual(s[11], Token('000', 'digit', 24, 27))
        self.assertEqual(s[9], Token('!!!!', 'punct', 19, 23))


class TestTokenizer(unittest.TestCase):  # class Tokenizer, method tokenize

    def setUp(self):
        self.t = Tokenizer()

    def test_first_alpha(self):
        s = 'я иду в кино cinema '
        self.assertEqual(self.t.tokenize(s), ['я', 'иду', 'в', 'кино', 'cinema'])

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
        self.assertEqual(self.t.tokenize(s), ['я', 'иду', 'в', 'кино', 'cinema'])

    def test_middle_nonapha(self):
        s = 'я иду в кино00000 111 00000cinema'
        self.assertEqual(self.t.tokenize(s), ['я', 'иду', 'в', 'кино', 'cinema'])

    def test_last_nonalpha(self):
        s = 'я иду в кино cinema!!!! 000'
        self.assertEqual(self.t.tokenize(s), ['я', 'иду', 'в', 'кино', 'cinema'])


class TestStringMethods(unittest.TestCase):  # function stringdiv

    def test_first_alpha(self):
        s = 'я иду в кино cinema '
        self.assertEqual(tokenizer.stringdiv(s), ['я', 'иду', 'в', 'кино', 'cinema'])

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
        self.assertEqual(tokenizer.stringdiv(s), ['я', 'иду', 'в', 'кино', 'cinema'])

    def test_middle_nonapha(self):
        s = 'я иду в кино00000 111 00000cinema'
        self.assertEqual(tokenizer.stringdiv(s), ['я', 'иду', 'в', 'кино', 'cinema'])

    def test_last_nonalpha(self):
        s = 'я иду в кино cinema!!!! 000'
        self.assertEqual(tokenizer.stringdiv(s), ['я', 'иду', 'в', 'кино', 'cinema'])
        

if __name__ == '__main__':
    unittest.main()
