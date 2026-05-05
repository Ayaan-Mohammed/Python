#Using Functions
def sqr(a):
    square=a*a
    print(square)

def cube(a):
    cube=a*a*a
    print(cube)

def large(a,b):
    if(a>b):
        return a
    
    else:
        return b
    

x=25
y=1025
z=158
sqr(x)
cube(x)
print(large(y, z))