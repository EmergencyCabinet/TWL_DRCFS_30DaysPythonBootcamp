
def cube(number):       
    result = number * number * number 
    print('The volume of cube is', result)

print (cube(3))

def cube(number):       
    result = number * number * number 
    print('The volume of cube is', result)
x = cube(3)
y = cube(9)
print ('The value of x is', x)
print('The value of y is', y)

def cube(number):       
    result = number * number * number 
    return result
x = cube(3)
y = cube(9)
z = x+y
print ('The sum of cube of 3 and 9 is', z)

def add(x,y):
    r = x+y
    return r
r = add(2,3)
r = add(5,10)
r = add(4,8)
print (r) # esto garda last ko matra print unxa kina ki every line ma r ko value change hudai xa

