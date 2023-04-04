#Wizard Game

is_magician = True
is_expert = False

#Check if magician AND expert: 'you are a master magician'

#Check if magician but not expert: 'At least you're getting there'

#Check if you're not a magician: 'you need magic powers man'

if is_magician and is_expert:
    print("you are a master magician") 
elif is_magician and not(is_expert):
    print("At least you're getting there")
else:
    print("You need magic powers")