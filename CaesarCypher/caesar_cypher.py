import random
import sys

key = random.randrange(1, 25, 1)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specialChars = [' ','.',',',':',';','*','!','@','#','$','%','^','&','(',')','?','/','<','>','[',']','{','}','+','=', '~', '`', '\'','_','-', '\"', '\\']
inputString = ''
argList = sys.argv

for word in argList:
    if argList.index(word) > 0:
        inputString += word + ' '

def lookupIndex(string):
    cypherString = ''

    for char in string:
        if char not in specialChars:
            capital = False

            if char.istitle():
                capital = True

            startIndex = alphabet.index(char.lower())
            cypherIndex = startIndex + key

            if (cypherIndex <= 25):
                if capital:
                    cypherString += alphabet[cypherIndex].upper()
                else:
                    cypherString += alphabet[cypherIndex]
            else:
                cypherIndex = cypherIndex - 26
                if capital:
                    cypherString += alphabet[cypherIndex].upper()
                else:
                    cypherString += alphabet[cypherIndex]
        else:
            cypherString += char
    return cypherString

print lookupIndex(inputString)
