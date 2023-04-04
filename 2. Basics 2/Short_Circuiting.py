# Short Circuiting

is_Friend = True
is_User = True

if is_Friend or is_User:
    print('best friends')
    
    
#What happens is that the machine does not care if is_User is true or false, because we are using "or"
#So it short circuits and goes faster and more efficiently.
