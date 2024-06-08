class CatProfile:
    def __init__(self, name, age, owner, state):
        self.name = name
        self.age = age
        self.owner = owner 
        self.state = state
        
        
    def Cat_name(self):
        print('The name of the cat is ' + self.name)
        
    def Cat_info(self):
        print('The owner of the cat is ' + self.owner + ' the age is ' , self.age)
            
cat1 = CatProfile('catty', 23, 'paul', 'kaduna')
cat2 = CatProfile('catty', 23, 'paul', 'kaduna')
cat3 = CatProfile('patty', 23, 'paul', 'kaduna')
cat4 = CatProfile('catty', 23, 'stonecond', 'new york')
cat5 = CatProfile('catty', 23, 'paul', 'kaduna')
cat6 = CatProfile('catty', 23, 'paul', 'kaduna')



print(cat3.name)
print(cat4.owner)
cat4.Cat_info()
cat5.Cat_name()