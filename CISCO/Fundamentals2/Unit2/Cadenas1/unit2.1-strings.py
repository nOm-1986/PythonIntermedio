"""
Las cadenas en python son secuencias inmutables
"""

string_multyline = '''
I can write multilines in python using three single quotes, or doble quotes
at the beging and another three in the end.
'''

string_two_quotes = """
Remember that specials characters like a \\ n count
"""

# String functions
# ord() - Show the ASCII 
char_1 = 'b'
char_2 = ' '
print(ord(char_1))
print(ord(char_2))

# chr() -- If you no the ASCII you can create its corresponding letter
# La función toma un punto de código y devuelve su carácter.
print(chr(20))
print(chr(97))
print(chr(945))


the_string = 'silly walks'

for ix in range(len(the_string)):
    if(the_string[ix] == ' '):
      print(the_string[ix], end='**')
    else: print(the_string[ix], end='-')

print()
print(the_string)


# We can also use chain slices
colombia = 'colombia'
print(colombia[3:-2])
print(colombia[1:5])
print(colombia[3:])
print(colombia[:2])
print(colombia[::2])
print(colombia[1::2])

# Compare string inside another string ON or NOT IN
vowels = 'aeiou'
print("a" in vowels) # True
print("b" in vowels) # False
struggle = "Another long string"
print('Anot' in struggle)
print("f" not in struggle)
print("F" not in struggle)
print("1" not in struggle)
print("A" not in struggle)

"""
min() -- max() -- index() -- list()
"""
print(min('aAbByYzZ')) # A -- 66
print(ord('a')) # 97
print("abcabc".count("b")) # 2
print('abcabc'.count("d")) # 0
print(list("abcabc")) # ['a', 'b', 'c', 'a', 'b', 'c']

x = '\''
print(len(x))

