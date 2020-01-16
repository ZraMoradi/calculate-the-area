from math import*



def squareArea(n):     #function of calculating area of square
    
        S=n*n
        print('the square area is',S)
    
def circleArea(n):       #function of calculating area of circle
       
        S=pi*r**2
        print('the circle area is',S)
    
def rectangleArea(n,m):       #function of calculating area of rectangle
        
        S=n*m
        print('the rectangle area is',S)
    
def triangleArea(n,m):         #function of calculating area of triangle
        
        S=(n*m)/2
        print('the triangle area is',S)
    
    

print('Please select the shape with the number(0,1,...)')
print('square,circle,rectangle,triangle')
i=int(input('enter the number:\n'))
if i==0:
    s=int(input('enter the square side:\n'))
    p=squareArea(s)
elif i==1:
    r=int(input('enter the radius of the circle:\n'))
    q=circleArea(r)
elif i==2:
    l=int(input('enter the length of the rectangle:\n'))
    w=int(input('enter the width of the rectangle:\n'))
    r=rectangleArea(l,w)
elif i==3:
    ru=int(input('enter the rule of the triangle:\n'))
    h=int(input('enter the height of the triangle:\n'))
    s=triangleArea(ru,h)
else :
    print('invalid number!')
