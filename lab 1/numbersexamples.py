#example 1
x=1
y=13.3
z=2j
print(type(x))
print(type(y))
print(type(z))
#int
#float
#complex

#example 2
x=45454545
y=23.1
z=-13
print(type(x))
print(type(y))
print(type(z))
#<class 'int'>
#<class 'float'>
#<class 'int'>

#example 3
x=14e3
y=13E2
z=-14.4e100
print(type(x))
print(type(y))
print(type(z))
#<class 'float'>
#<class 'float'>
#<class 'float'>

#example 4
x=float(2)
y=int(4.8)
z=complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
#2.0
#4
#(1+0j)
#<class 'float'>
#<class 'int'>
#<class 'complex'>
