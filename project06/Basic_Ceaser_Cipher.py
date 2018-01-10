# Basic Ceaser Cipher

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

def get_func():
    print('Do you want to (e)ncrypt or (d)ecrypt a Message?')
    func = input()
    function = func[0]
    return function

def get_msg():
    print('Enter Secret Message')
    msg = input().upper()
    return msg

def get_key():
    print('Select a key shift')
    key = int(input())
    return key
    
function = get_func()
msg = get_msg()
key = get_key()

# Start the translation
for chr in msg:
    if chr in LETTERS:
        num = LETTERS.find(chr)

        if function == 'e':
            num = num + key
        elif function == 'd':
            num = num - key

# Sort the wrap around problem, so that it acts like a ceaser wheel
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

# Start to build the translated string
        translated = translated + LETTERS[num]

    else:
        translated = translated + chr

# Print the result
print(translated)
