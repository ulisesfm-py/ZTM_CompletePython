#Our first GUI Graphical User Interface

import numpy as np

#list of lists
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
    ]

for image in picture:
    for pixel in image:
        if(pixel ==1):
            print('*' , end='')
        else:
            print(' ', end='')
    print('')
            