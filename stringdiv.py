""" This module converts an input string to a list of alphaberical substrings"""

string = input()
def stringdiv(string):
    """ Divides a string in a list of alphabetical substrings.

    @param string: a string
    @return a list of alphabetical substrings
    """
    
    listwords = []
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
        listwords.append(string[i:index+1])
        
    return listwords

result = stringdiv(string)
print(result)

  

        
