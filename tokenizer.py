"""
This module contains different methods and a function for tokenizing a string of characters
"""
import unicodedata


def stringdiv(string):
    """ Divides a string in a list of alphabetical substrings.

    @param string: a string
    @return a list of alphabetical substrings
    """
    listwords = []
    if len(string) == 0:
        listwords = []
    else:
        for index, char in enumerate(string):
            # find the beginning of an alpha substring
            # it is either the first char in string
            # or the char that is alpha, but the previous one is not
            if char.isalpha() and (index == 0 or not string[index-1].isalpha()):
                i = index
            
            # making sure that we didn't reach the last char of the string
            if (index + 1) <= (len(string) - 1) and char.isalpha() and not string[index + 1].isalpha():
                # find the end of alpha substring and add it to list
                if char.isalpha() and not string[index+1].isalpha():
                    listwords.append(string[i:index+1])
                
        # check the last char in the string
        # add to the list if it is alpha
        if char.isalpha():
            listwords.append(string[i:])

    return listwords


class Tokenizer(object):
    """
    This class contains methods for tokenizing a string

    """
    def tokenize(self, string): 
        """ This method divides a string in a list of alphabetical substrings.

        @param string: a string 

        @return a list of alphabetical substrings (tokens)

        """
        listwords = []
        if len(string) == 0:
            return []
        else:
            for index, char in enumerate(string):
                # find the beginning of an alpha substring
                # it is either the first char in string
                # or the char that is alpha, but the previous one is not
                if char.isalpha() and (index == 0 or not string[index-1].isalpha()):
                    i = index
            
                # making sure that we didn't reach the last char of the string
                if (index+1) <= (len(string)-1):
            
                    # find the end of alpha substring and add it to list
                    if char.isalpha() and not string[index+1].isalpha():
                        listwords.append(string[i:index+1])
                
            # check the last char in the string
            # add to the list if it is alpha
            if char.isalpha():
                listwords.append(string[i:])

            return listwords

    @staticmethod
    def catdef(char):

        """ this method is used for determining categories of chars in the string """
        
        if char.isalpha():
            category = 'alpha'
        elif char.isdigit():
            category = 'digit'
        elif char.isspace():
            category = 'space'
        elif unicodedata.category(char)[0] == 'P':
            category = 'punct'
        else:
            category = 'unknown'
        return category

    def tokenize_categories(self, string):
        """
        This method tokenizes a string and
        adds token, its category, index of first and last char of substring in initial string
        it also creates an instance of class Token with attributes and prints it
        @param string: a string
        @return a list of instances of class Token with attributes - (substring, its category, first index, last index)
        """
        listwords2 = []
        if len(string) == 0:
            return []
        else:
            for index, char in enumerate(string):
                # determine category of char
                category = self.catdef(char)

                # find the beginning of an substring of one category
                # it is either the first char in string
                # or the char of one category, but the previous one of another
                # we save category after loops in order not to call catdef when it is unnecessary
                if index == 0:
                    i = index
                    prevcat = category
                # making sure that we didn't reach the last char of the string
                elif (index+1) < len(string):
                    # find the end of substring of one and add it to list
                    # to do so we compare categories of current and next chars
                    # if they are different - we have reached the last char of the category and we add the substring
                    if category != prevcat:
                        token = string[i:index]
                        t = Token(token, prevcat, i, index)
                        listwords2.append(t)
                        i = index
                        prevcat = category  # memorising the category

            # check the last char in the string if it wasn't checked before
            # it will be a char of another category
            # and also when all chars of the same category like 012345
            token = string[i:]
            # index = index + 1
            t = Token(token, category, i, index) # ?? what should we take as index
            listwords2.append(t)
            
        return listwords2

        
class Token(object):
    """
    Class for tokens with substring of the string, category of the substring
    and its first and last indexes in the string as attributes of the class
    """

    def __init__(self, t, cat, fi, li):
        """ Here we initialize the attributes of a class """
        
        self.token = t
        self.category = cat
        self.firstindex = fi
        self.lastindex = li

    def __repr__(self):
        """ This method is used to return a printable representation of the object"""

        # we need to covert int to str implicitly for this method to work properly
        return '(' + self.token + ':' + self.category + ', [' + str(self.firstindex) + ', ' + str(self.lastindex) + '])'

    def __eq__(self, other):
        """Compares instances of class Token.
        If the attributes of the elements are equal,
        then the attributes themselves are equal"""

        # we need to check that we are dealing with an instance of class Token
        if isinstance(other, Token):
            return (self.token == other.token and
                    self.category == other.category and
                    self.firstindex == other.firstindex and
                    self.lastindex == other.lastindex)
        # if the other element is not an instance of class Token, we can't compare them
        # NotImplemented is a special value which should be returned by the binary special methods
        # to indicate that the operation is not implemented with respect to the other type
        return NotImplemented


def main():
    t = Tokenizer()
    string = 'i want 2 be!!!!'
    print(t.tokenize(string))
    result = stringdiv(string)
    print(result)
    print(t.tokenize_categories(string))
   

if __name__ == '__main__':
    main()
