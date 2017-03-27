# times_table app

name = input('What is your name? ')
print('Hello', name)

number = int(input('What times table would you like to do? '))
iteration = int(input('How many times should we do this? '))

#def times_table(num):
n = 1
while n <= iteration:
    print(n, "x", number, "=", n*number)
    n=n+1

#times_table(number)
