
### Syntax Errors  ####

# SyntaxError
'''
print('hello 1')

 print('hello 2')
'''

# SyntaxError
'''
a = 10
print a
'''

# SyntaxError
'''
if 10 > 5:
    print('hello 1')
    print('hello 2')

print('hello hi')

else:
    print('hello 3')
    print('hello 4')
'''

# SyntaxError
'''
for  in range(10):
    print(i)

'''

# SyntaxError
'''
def add(x=10,y):
    print(x)
    print(y)
    print(x + y)

add(20)
'''

# SyntaxError
'''
def add(x,y=20):
    print(x)
    print(y)
    print(x + y)

add(y=25,30)
'''


### Working with Runtime  Errors  ####

#IndexError: list index out of range
'''
print('start line')

lst = [10,20,30]

print(lst[4])

print('end line')
'''


# Using without exception handling  returns FileNotFoundError:
'''
print('start line')

fileobject = open('demo.txt', 'r') 

print('end line')
'''

# Using exception handling returns user friendly message
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r')
except:
    print('Given file name not available')

print('end line')
'''

## if raised exception class is  handling  proprly by excepty block then returns exception message
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError
    
except FileNotFoundError:
    print('Given file name not available')

print('end line')
'''

## if raised exception class is not handling by excepty block then returns exception
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError
    
except NameError:
    print('Given file name not available')

print('end line')
'''

## Working with "else" block ###
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError
    
except NameError:
    print('Given file name not available')

else:
    data = fileobject.read()
    print(data)
    
print('end line')
'''

# try block with multiple named exception blocks
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError

except NameError:
    print('Error : NameError returns')

except ValueError:
    print('Error: ValueError returns')
    
except FileNotFoundError:
    print('Given file name not available')

else:
    data = fileobject.read()
    print(data)
    
print('end line')
'''

#  try block with multiple named exception blocks and defalt except block
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError

except NameError:
    print('Error : NameError returns')

except ValueError:
    print('Error: ValueError returns')
    
except KeyError:
    print('Given file name not available')

except:
    print('Some thing wrong')
else:
    data = fileobject.read()
    print(data)
    
print('end line')
'''


## SyntaxError
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError

except NameError:
    print('Error : NameError returns')

except ValueError:
    print('Error: ValueError returns')

except:
    print('Some thing wrong')
    
except KeyError:
    print('Given file name not available')


else:
    data = fileobject.read()
    print(data)
    
print('end line')

'''


## Working with  "as" keyword (Creating exceptuion variable using "as" keyword)
'''
print('start line')

try:
    x = 10 / 0 # ZDE

except NameError as e:
    print("Error:",e)

except ZeroDivisionError as e:
    print("Error:",e)
    
else:
    print("Result :",x)
    
print('end line')
'''

# What is output?
'''
print('start line')

try:
    x = 10 / 2 # 

except NameError as e:
    print("Error:",e)

except ZeroDivisionError as e:
    print("Error:",e)
    
else:
    print("Result :",x)
    
print('end line')
'''

## How to grouping multiple exceptions using single except block
'''
print('start line')

try:
    n1 = eval(input('Enter first number :')) # 10
    n2 = eval(input('Enter second number :'))# 2
    result = n1 / n2 # 

except (NameError, ValueError,ZeroDivisionError) as e:
    print("Error:",e)
    
else:
    print("Result :",result)
    
print('end line')
'''

# What is output?
'''
print('start line')

try:
    n1 = eval(input('Enter first number :')) # 10
    n2 = eval(input('Enter second number :'))# 'a'
    result = n1 / n2 # TypeError

except (NameError, ValueError,ZeroDivisionError) as e:
    print("Error:",e)
    
else:
    print("Result :",result)
    
print('end line')
'''

# What is output
'''
print('start line')

try:
    n1 = eval(input('Enter first number :')) # 10
    n2 = eval(input('Enter second number :'))# a
    result = n1 / n2 # NameError

except (NameError, ValueError,ZeroDivisionError) as e:
    print("Error:",e)
    
else:
    print("Result :",result)
    
print('end line')
'''

###
'''
try:
    pass

except NameError as e:
    pass

except TypeError as e:
    pass

except (ValueError,KeyError, ZeroDivisionError) as e:
    pass

except:
    pass

else:
    pass
'''

### Working combination blocks
'''
try:
    pass

except NameError:
    pass

except ValueError:
    pass

except:
    pass

else:
    pass

finally:
    pass
'''


## How to creating fileObject resource ?
'''
print('start line')

fileObject = None

try:
    fileObject = open('demo.txt', 'r')
    
except FileNotFoundError as e:
    print("Error :", e)

else:
    data = fileObject.read()
    print(data)

finally:
    if fileObject:
        fileObject.close()
                
print('end line')
'''




## Working with nested blocks
'''
print('start line')

try:
    print('try-1 block')
    try:
        print('try-2 block')
    except:
        print('except-2 block')
    finally:
        print('finally-2 block')
except:
    print('except-1 block')
finally:
    print('finally-1 block')

print('end line')

'''

# What is output
'''
print('start line')

try:
    print('try-1 block')
    n1 = eval(input('Enter first number :')) # 
    n2 = eval(input('Enter second number :'))# 
    result = n1 / n2 #
    print('Result :', result)
    try:
        print('try-2 block')
    except:
        print('except-2 block')
    finally:
        print('finally-2 block')
except ValueError:
    print('except-1 block')
finally:
    print('finally-1 block')

print('end line')
'''


## What is output?
'''
print('start line')

try:
    print('try-1 block')
    n1 = eval(input('Enter first number :')) # 10
    n2 = eval(input('Enter second number :'))# 'a'
    
    try:
        print('try-2 block')
        result = n1 / n2 # TypeError
        print('Result :', result)
    except NameError as e:
        print('except-2 block')
        print('Error:',e)
    finally:
        print('finally-2 block')
except TypeError:
    print('except-1 block')
finally:
    print('finally-1 block')

print('end line')
'''

#### Working with  Userdefined Exceptions ####  


class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass  

default_number = 10

while True:
    try:
        user_number = int(input('Enter any number :')) # 'a' ,  5 ,  15 , 10 ,

        if user_number < default_number: # 5 < 10
            raise ValueTooSmallError
        
        elif user_number > default_number: # 15 > 10
            raise ValueTooLargeError

        elif user_number == default_number:
            print('Congrats! Your guess is currect!')
        break            

    except ValueTooSmallError:
        print('User entered value too small number than default value')

    except ValueTooLargeError:
        print('User entered value too large number than default value')

        
    except Exception as e:
        print('Error :',e)
        
        
    











