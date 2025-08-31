"""
int - Whole number 100 200 -100
float - Decimal numbers 1.345
complex - Real and Imaginary part 
"""
a = 10;
b = 10.5;
c = 3+5;

print(a, b, c);
print(type(a), type(b), type(c));

"""
Boolean data types
None data type - Kuchh bhi nhi
sequence data types - Multiple value store only in one data type
string - "" or '' ---> Group of words or character
"""
text = "This a words"
print(text);

"""
List Data type  - 
"""
my_list = ['data1', 'data2', 'data3'];
print(my_list)

"""
set data type --> Mutable set and Immutable set
"""
unique_number = {1, 2, 3, 4, 2, 1, 3};
print(unique_number) #Mutable set

unique_number1 = frozenset([1, 2, 3, 4, 4, 5]);
print(unique_number1)