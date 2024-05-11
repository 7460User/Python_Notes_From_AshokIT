

##
'''
print('start line')

for i  in  'python':
    print(i)
    
print('end line')
'''


#
'''
print('start line')

for i  in  'python':
    print(i, end="\n")
    
print('end line')
'''


#
'''
print('start line')

for i  in  'python':
    print(i, end=" ")

print()

print('end line')
'''

# What is output
'''
for i  in range(5): # range(0,5,1) # 0,1,2,3,4
    print(i) 

'''


# What is output

'''
print('Welcome')
print('Welcome')
print('Welcome')
print('Welcome')
print('Welcome')

print('Welcome')
print('Welcome')
print('Welcome')
print('Welcome')
print('Welcome')
'''

# What is output
'''
for i in range(10):
    print('Welcome')
'''


##
'''
for _ in range(10):
    print('Welcome')
    
'''


## Display given n'th number table
'''
n = int(input('Enter any number :')) # 5

for i in range(11):
    print(n ,"*", i,"=",  n * i)
'''   

##### working with  while loop #####

'''
print('start line')

i = 0
while i < 5:  #  0 < 5, 1 < 5, 2 < 5, 3 < 5, 4 < 5, 5 < 5
    print('Hello',i)

    i = i + 1 #  1, 2, 3, 4, 5

print('end line')
'''

# What is output
'''
print('start line')

i = 5
while i > 0:  #  
    print('Hello',i)

    i = i - 1 #  4,3,2,1,0

print('end line')
'''

##### Transfer | Jump Statements ######


## break
'''
for i  in  range(10):  # 0,1,2,3,4,5,6,7,8,9
    if i == 3:
        break
    print('value :',i)

print('outside for loop')
'''


## continue
'''
for i  in  range(10):  # 0,1,2,3,4,5,6,7,8,9
    if i == 3:
        continue
    print('value :',i)

print('outside for loop')
'''


## break  and continue
'''
for i  in  range(10):  # 0,1,2,3,4,5,6,7,8,9
    if i == 3:
        continue
    if i == 7:
        break
    print('value :',i)

print('outside for loop')
'''

##  working with "pass"  keyword


# SyntaxError
'''
if 10 > 5:
    
else:
    print('Condition Returns False')
'''

#
'''
if 10 > 5:
    pass
else:
    print('Condition Returns False')
'''


'''
for i  in range(5):
    pass
'''


'''
i = 0
while i < 5:
    pass
'''


## working with  "for - else"  combination
'''
for i in range(5): # 0,1,2,3,4
    print(i)

else:
    print('For loop executed successfully!')

print('End line')
'''

## What is output
'''
for i in range(5): # 0,1,2,3,4
    if i == 2:
        break
    print(i)

else:
    print('For loop executed successfully!')

print('End line')
'''

## What is output
'''
for i in range(5): # 0,1,2,3,4
    if i == 2:
        continue
    print(i)

else:
    print('For loop executed successfully!')

print('End line')
'''


## working with  "return" keyword
'''
def message():
    print('hello 1')
    print('hello 2')
    print('hello 3')

message()    
'''

'''
def message():
    print('hello 1')
    print('hello 2')
    print('hello 3')
    return None

print(message())  
'''

'''
def message():
    print('hello 1')
    print('hello 2')
    print('hello 3')
    return "hello"

print(message())
'''

#  What is output?
'''
def  addition(a,b):
    return a + b

x = addition(10,20)
print(x)
'''

## What is output?
'''
def message():
    print('hello 1')
    print('hello 2')
    print('hello 3')
    return "hello"
    print('hi')
    print('Welcome')
    
print(message())
'''

## working with "assert" keyword

n = int(input('Enter any number :'))  

assert n > 0, "Entered number is negative number"
print('Entered number is a positive number')
print('We are proceessing your request')












    




















