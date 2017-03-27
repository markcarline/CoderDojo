# Fibonacci Sequence

a = 0
b = 1

while b < 5000:
    print(b)
    a, b = b, a + b  # a will now be 1, and b will also be 1, (0 + 1) because
                     # the sum of b is evaluated before a is increased to 1
    
    
