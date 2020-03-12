a=int(input('enter the first number'))
b=int(input('enter the second number'))
c=int(input('enter the third number'))
maximum=a
minimum=a
if b>a:
    maximum=b
else:
    minimum=b
if c>maximum:
    maximum=c
if c<minimum :
    minimum=c
print( maximum ,'is max')
print( minimum ,'is min')
