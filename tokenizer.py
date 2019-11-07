""" This module contains methods and a function for tokenizing a string of characters
    
"""

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
            # or the char that is alpha, but the previos one is not
            if char.isalpha() and (index == 0 or not string[index-1].isalpha()):
                i = index
            
            # making sure that we didn't reach the last char of the string
            if (index+1)<=(len(string)-1):
            
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
                # or the char that is alpha, but the previos one is not
                if char.isalpha() and (index == 0 or not string[index-1].isalpha()):
                    i = index
            
                # making sure that we didn't reach the last char of the string
                if (index+1)<=(len(string)-1):
            
                    # find the end of alpha substring and add it to list
                    if char.isalpha() and not string[index+1].isalpha():
                        listwords.append(string[i:index+1])
                
            # check the last char in the string
            # add to the list if it is alpha
            if char.isalpha():
                listwords.append(string[i:])

            return listwords
            
def main():
    t = Tokenizer()
    string = input()
    print(t.tokenize(string))
    result = stringdiv(string)
    print(result)

if __name__ == '__main__':
    main()


    



        

    
