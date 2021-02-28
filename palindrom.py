#palindromy

def palindrom(text):
    i=int(len(text)/2) #połowa długości tekstu
    for index in range(i):
        if text[index]==text[-(index+1)]: #sprawdzanie kolejnych znaków
            continue
        else:
            return False
    return True


#sprawdzenie działania funkcji
to_check=['ada', 'kajak', 'pies', 'zakaz', 'abccba', 'drzewo', 'radar', 'abba', 'oko', 'dziecko']
for word in (to_check):
    if(palindrom(word)):
        print(word, " jest palindromem")
    else:
        print(word, " nie jest palindromem")
