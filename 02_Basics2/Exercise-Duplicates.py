#Exercise about duplicates

#Check for duplicates in list

some_list = ['a' , 'b' , 'c' , 'b' , 'd' , 'm' , 'n' , 'n']

index_i = 0

for i in some_list:
    
    index_j = 0
    duplicates = 0
    
    for j in some_list:
        
        if i == j:
            duplicates += 1
            
        if duplicates > 1:
            print('we found a duplicate of ', i, 'in positions:', index_j)
            duplicates -=1
        
        index_j += 1
    index_i += 1
    
#Now the solution

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
        
print(duplicates)
            
        
    

