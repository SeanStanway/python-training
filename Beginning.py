def print_function(exampleName, content):
    return '{} {}'.format(exampleName, content)
def newLine():
    return ''

def my_function():
    a = 2
    return a
print(print_function("Function:", my_function()))

print(newLine())

b = 5
c = 7
if b > c:
    print(print_function('If Statement:', 'b is more than c'))
else:
    print(print_function('If Statement:','c is more than b'))

print(newLine())

import math
newMath = math.sqrt(16)
print(print_function('Math Import:', newMath))

print(newLine())

int_list = [1, 2, 3]
string_list = ['test', '123']
nested_list = [['nest', 'two'], [100, 200]]
print(print_function('Int List:', int_list))
print(print_function('Int List, Single Value:', int_list[1]))
print(newLine())
print(print_function('String List:', string_list))
print(print_function('String List, Negative Counting ([-2]):',string_list[-2]))
print(newLine())
print(print_function('Nested List:', nested_list))
print(print_function('Nested List, Single Value:', nested_list[0][1]))
nested_list[0][1] = 'New Stuff'
print(print_function('Nested List, Mutated Value', nested_list))
int_list.insert(3, 4)
print(newLine())
print(print_function('Int List, Insert:', int_list))
int_list.remove(2)
print(print_function('Int List, Remove', int_list))
print(print_function('Int List, Len(gth):', len(int_list)))
print(print_function('String List, Index Location:', string_list.index('123')))
print(newLine())
print('-----For Loop')
for element in int_list:
    print (element)
print('-----For Loop END')
