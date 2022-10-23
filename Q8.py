#Write a python program to multiply all the numbers in a list.

def mul(*t):
    bag=1;
    for a in t:
        if a==0:
         bag=bag*1
        else: 
         bag=bag*a
    print(bag)    
list=[3,2,9,0,3,2,0,5]  
mul(*list) 