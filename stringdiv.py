string = input()
def stringdiv(string):
    listwords = []
    for index, char in enumerate(string):
        if char.isalpha() and (index == 0 or not string[index-1].isalpha()):
            i = index
        if (index+1)<=(len(string)-1):
            if char.isalpha() and not string[index+1].isalpha():
                listwords.append(string[i:index+1])
    if char.isalpha():
        listwords.append(string[i:index+1])
    return listwords;
result = stringdiv(string)
print(result)
  

        
