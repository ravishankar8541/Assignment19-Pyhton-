#Write a python program to create a function which expects an unknown number of
#arguments.

def add(*t):
    a=sum(t)
    return a
print("sum =",add(8,9,3))
print("sum =",add(6,3,2,2,56,5))    
print("sum =",add(7))