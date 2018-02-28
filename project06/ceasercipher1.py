# Ceaser cipher
KEY_SPACE = 26

def getMechanism():
    while True:
        print('Do you want to encrypt or decrypt a message?')
        mechanism = input().lower()
        if mechanism in 'encrypt e decrypt d'.split():
            return mechanism
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter Secret Message')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key (1-%s)' % (KEY_SPACE))
        key = int(input())
        if (key >= 1 and key <= KEY_SPACE):
            return key

def getTranslatedMessage(mechanism, message, key):
    if mechanism[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num +=key

            if symbol.isupper():
                if num > ord('Z'):
                             num -= 26
                elif num < ord('A'):
                             num += 26
            elif symbol.islower():
                if num > ord('z'):
                             num -=26
                elif num < ord('a'):
                             num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mechanism = getMechanism()
message = getMessage()
key = getKey()

print('Your translated text is:')
print(getTranslatedMessage(mechanism, message, key))

    
