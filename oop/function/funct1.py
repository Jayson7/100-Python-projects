# args: positional arguments
# parameters: arguments that are passed to a function
# *****************************************************************************
# a basic function 
# name = 'john'
# def namer2():
#     print("Hello " + name)
    
# namer2()

# *****************************************************************************
def namer(name):
    print("Hello " + name)

    return 'hello ' +   name
print(namer('john'))
print(namer('jane'))

# *****************************************************************************
# kwargs: keyword arguments
# what is kwargs ? 

# kwargs is a dictionary

# *****************************************************************************
def namer(name, age):
    print("Hello " + name)
    print("You are " + str(age))
namer('john', 30)
namer('jane', 25)
namer(name='john', age=30)    
# ******************************************************************************
# args example
def food(*args):
    print(args)
food('apple', 'banana', 'orange')
# ******************************************************************************
def cars(make):
    return make
print(cars(make={'maker':'bmw', 'model':'x5'}))
# kwargs example
def food(**kwargs):
    print(kwargs)
device = {'maker':'apple', 'model':'iphone'}
food(name='apple', age=30, city='new york', device = {'maker':'apple', 'model':'iphone'})

