LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

getFunc = input('Do you want to (e)ncrypt or (d)ecrypt\n')
function = getFunc[0]

sentence = input('Enter secret message\n')

#remove all spaces from sentence (to get length) and create an upper case version
sentenceRem = sentence.replace(' ','')
lenSentence = len(sentenceRem)
upperSentence = sentence.upper()

#We need a key
key = input('Enter a key\n')

#repeat key as many times as needed and create upper case version
lenKey = len(key)
amt = int(lenSentence/lenKey)
amt2 = lenSentence % lenKey
repeatingKey = (key*int(amt)) + key[0:amt2]
upperRepKey = repeatingKey.upper()

#Do the crypto
numPos = 0
for chr in upperSentence:
    if chr in LETTERS:
        num = LETTERS.find(chr)
        keyLetter = upperRepKey[numPos]
        keyVal = LETTERS.find(keyLetter)
        if function == 'e':
            result = (num + keyVal) % len(LETTERS)
        else:
            result = (num - keyVal) % len(LETTERS)

        translated = translated + LETTERS[result]
        numPos += 1

    else:
        translated = translated + chr

print(translated)
