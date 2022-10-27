import black
import cv2
import numpy as np
import math

def rotate(step,data):
    for x in(len(step)):
        if step[x]=='R':
            rotate
        elif step[x]=='Rb':
            rotate
    return(data)


data=['cube_color_data']

#need 2 find the front side
#but how 2 find


#----------------------bottom and mid----------------------- F2L alot
    # need to find how to find it and can start write here
    #first rotate the corner the the right side top or mid
    #and find where the side part is





#----------------------top -----------------------OLL1-57
#https://maru.tw/oll-pll/
while(True):
    if data=='OLL01':
        step=['R','U', 'U', 'R', 'R',' F' ,'R' ,'Fc' ,'U' ,'U',' Rc','F','R','Fc'] #R U'2 R2 F R F' U2 R' F R F'
        break
    if data=='OLL02':
        step=['F','R', 'U', 'Rc', 'Uc',' Fc' ,'B' ,'U' ,'L' ,'Uc',' Lc','Bc'] #F R U R' U' F' B U L U' L' B'
        break
    if data=='OLL03':
        step=['Lc','R','R','B','Rc','B','L','U','U','Lc','B','Rc','L']#L' R2 B R' B L U2 L' B R' L
        break
    if data=='OLL04':
        step=['R','L','L','Bc','L','Bc','Rc','U','U','R','Bc','Rc','L']#R L2 B' L B' R' U2 R B' R' L
    if data=='OLL25':
        step=['Fc','L', 'F', 'Rc', 'Fc','Lc' ,'R' ,'R'] #F' L F R' F' L' F R   
        break
    if data=='OLL26':
        step=['R','U', 'U', 'Rc', 'Uc','R' ,'Uc' ,'Rc'] #R U2 R' U' R U' R'
        break
    if data=='OLL44':
        step=['F','U', 'R', 'Uc', 'Rc','Fc'] #F U R U' R' F'
        break
    if data=='OLL57':
        step=['R','U', 'Rc', 'Uc', 'Rc','L','F','R','Fc','Lc'] #R U R' U' R' L F R F' L'
        break

#----------------------top side-----------------------PLL1-21
#https://maru.tw/oll-pll/
while(True):
    if data=='top_trangle_mid_cw' : #top side mid trangle transformer PLL01
        step=['R','R', 'U', 'R', 'U',' Rc' ,'Uc' ,'Rc' ,'Uc' ,'Rc',' U','Rc'] #R2 U R U R' U' R' U' R' U R'
        break

    if data=='top_trangle_mid_ccw':#top side mid trangle transformer PLL02
        step=['R','Uc',' R',' U',' R',' U','R',' Uc',' Rc',' Ub' 'R','R'] #R U’ R U R U R U’ R’ U’ R2
        break
    if data=='top_trangle_angle_ccw':#top side angle trangle transformer PLL03
        step=['R',' Bc' ,'R', 'F','F' ,'Rc' ,'B',' R', 'F','F','R','R'] #R B' R F2 R' B R F2 R2
        break
    if data=='top_trangle_angle_cw':#top side angle trangle transformer PLL04
        step=['R',' R' ,'F' ,'F','Rc' ,'Bc' ,'R',' F', 'F','Rc','B','Rc'] # R2 F2 R' B' R F2 R' B R'
        break
    if data=='top_side_z_transform':#top side mid Z transformer PLL05
        step=['Rc',' Uc' ,'R' ,'Uc','R' ,'U' ,'R',' Uc', 'Rc','U','R','U','R','R','Uc','Rc','U','U'] # R' U' R U' R U R U' R' U R U R2 U' R' U2
        break
    if data=='top_side_H_transform':#top side mid H transformer PLL06
        step=['R',' R' ,'U' ,'U','R' ,'R' ,'U',' U', 'R','R','Uc','R','R','U','U','R','R','U','U','R','R','U'] # R2 U2 R2 U2 R2 U' R2 U2 R2 U2 R2 U
        break






rotate(step)