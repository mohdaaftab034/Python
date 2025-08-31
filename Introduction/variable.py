# Variable and Its types

# Variable: Variable is a my_name given to a memory location in a program.

my_name = "Mohd Aaftab"
age = 20
price = 25.50

print("My my_name is ",my_name)
print("My age is ",age)

# Rules for identifiers: 
# 1. Identifiers can be combination of uppercase and lowercase letters, digits, or an underscore(_). So myVariable , vaiable1, variable2, variable_for_print all are valid Python identifiers
# 2. An identifiers can not start with digit, So while variable1 is valid, 1variable is not valid


# Types: Python automatically detect the what type of data type
print(type(my_name))
print(type(age))
print(type(price)) 

my_name1 = "MA"
my_name2 = 'MA'
my_name3 = '''MA'''

print(my_name1)
print(my_name2)
print(my_name3)

#Boolean data types is started a first letter is capital letter
age = 23
old = False
a = None

print(type(old))
print(type(a))

#Types of tokens - Punctuators are symbols to organize sentance structure in programming

#Expression Execution

a, b = 2, 3
Txt = "@"
print(a*Txt*b)

c, d = "2", 3
print((c+Txt) * d)

e, f = 100, .5
h = e * f
print(h)

#Floor gives closest integer, which is lesser then or equal to the float value
# Result of (A//B) is same as floor(A/B)
A, B = 12, 5
C = A//B
print(C)