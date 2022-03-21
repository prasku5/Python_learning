# 'Print' is a function in python 3
# Below one's are just statements but not function and dont return a value (provides instruction or commands for Python to perform)

# Syntax
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# Addition of two numbers
from time import sleep
print(2+3)

# Python converts everything into a string (default delimiter is ' ')
print('Python', 3, 'Rocks')

print('Python', 3, 'Rocks', sep=',')

# You can set the end argument to a whitespace character string to print to the same line in Python 3.
print('Python', 3, 'Rocks', end=' ')
print('I love Python')


print('Python', 3, 'Rocks', end=',')
print('I love Python')


print('Python', 3, 'Rocks', end='*')
print('I love Python')

# Printing to a file

print('Hello World', file=open('hello.txt', 'w'))

# Flush the buffer immediately

print('Will it get printed immediately?', end='', flush=True)
sleep(5)


# print over and over the same line in Python, you have to use the
# carriage return \r symbol with the end argument.

print("Pylenin", end="\r")
print("loves", end="\r")
print("Python")

# Even though the first 2 print statements are executed, the carriage return makes the next stdout line start at the beginning of the current line.
# Also, carriage return will only replace the number of characters contained in the print statement. That is the reason, you have an extra n at the end.

# Source credit: https://www.pylenin.com/blogs/python-print/
