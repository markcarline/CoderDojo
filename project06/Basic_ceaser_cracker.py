# Basic Ceaser Cracker

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_msg():
    print('Enter the Secret Message you want to crack')
    msg = input().upper()
    return msg
    
msg = get_msg()

# Try every possible key
for key in range(len(LETTERS)):

    translated = ''

# Start the translation
    for chr in msg:
        if chr in LETTERS:
            num = LETTERS.find(chr)

            num = num - key

            if num < 0:
                num = num + len(LETTERS)

# Start to build the translated string
            translated = translated + LETTERS[num]

        else:
            translated = translated + chr

# Print the result
    print('Key %s:  %s' % (key, translated))
