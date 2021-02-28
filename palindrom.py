#palindromy

def palindrome(text):
    """
        Checks if given argument is palindrome. Returns True or False
        Arguments:
        text - string to be checked
    """
    i=int(len(text)/2) #half of text length
    for index in range(i):
        if text[index]==text[-(index+1)]: #check characters
            continue
        else:
            return False
    return True


#check
to_check=['ada', 'kajak', 'pies', 'zakaz', 'abccba', 'drzewo', 'radar', 'abba', 'oko', 'dziecko']
for word in (to_check):
    if(palindrome(word)):
        print(word, " jest palindromem")
    else:
        print(word, " nie jest palindromem")

help(palindrome)
