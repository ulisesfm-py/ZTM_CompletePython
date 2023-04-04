#Iterables

for item in 'Zero to Mastery':
    print(item)
    
for item in (1,2,3,4,5):
    for x in ['a', 'b' , 'c']:
        print(item , x)
        
#Iterables - list, dictionary, tuple, set, string

#Let's create a dictionary user

user = {
        'name': 'Golem',
        'age' : 5006,
        'can_swim' : False}

for item in user.items():
    print(item)
    
for item in user.values():
    print(item)

for item in user.keys():
    print(item)
    
#What if we wanna print separately

for key, value in user.items():
    print(key, value)

    



