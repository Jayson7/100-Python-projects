#  x a global variable
x = 5  

def checker():
    global c
    c =6
    print(c)
    if x == 5:
       print ('True')
    else:
       print ('False')
    
checker()
print(c)
print(x)
