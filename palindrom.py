#palindromy

def palindrom(text):
    i=int(len(text)/2) #połowa długości tekstu
    for index in range(i):
        if text[index]==text[-(index+1)]: #sprawdzanie kolejnych znaków
            continue
        else:
            return False
    return True