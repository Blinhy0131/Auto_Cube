import black
import cv2
import numpy as np
import math

def rotate(step,data):
    for x in(len(step)):
        if step[x]=='R':
            rotate
        elif step[x]=='Rb':
            for i in range(3):
                rotate
        elif step[x]=='L':
            rotate
        elif step[x]=='Lc':
            for i in range(3):
                rotate
        elif step[x]=='F':
            rotate
        elif step[x]=='Fc':
            for i in range(3):
                rotate
        elif step[x]=='B':
            rotate
        elif step[x]=='Bc':
            for i in range(3):
                rotate
        elif step[x]=='U':
            rotate
        elif step[x]=='Uc':
            for i in range(3):
                rotate
    return(data)


data=['cube_color_data']

#need 2 find the front side
#but how 2 find

#----------------------bottom side -----------------------
    #the first step need to find the 4 side of the bottom side
    #1.know the bottom color
    #2.find the color of the side
    #3.how 2 rotate?

#----------------------bottom and mid----------------------- F2L alot
    # need to find how to find it and can start write here
    #first rotate the corner the the right side top or mid
    #and find where the side part is





#----------------------top -----------------------OLL1-57
#https://maru.tw/oll-pll/
while(True):
    oll_type=1 #just for tset
    if oll_type==1:
        step=['R','U', 'U', 'R', 'R',' F' ,'R' ,'Fc' ,'U' ,'U',' Rc','F','R','Fc'] #R U'2 R2 F R F' U2 R' F R F'
        break
    if oll_type==2:
        step=['F','R', 'U', 'Rc', 'Uc',' Fc' ,'B' ,'U' ,'L' ,'Uc',' Lc','Bc'] #F R U R' U' F' B U L U' L' B'
        break
    if oll_type==3:
        step=['Lc','R','R','B','Rc','B','L','U','U','Lc','B','Rc','L']#L' R2 B R' B L U2 L' B R' L
        break
    if oll_type==4:
        step=['R','L','L','Bc','L','Bc','Rc','U','U','R','Bc','Rc','L']#R L2 B' L B' R' U2 R B' R' L
        break
    if oll_type==9:
        step=['R','U','Rc','Uc','Rc','F','R','R','U','Rc','Uc','Fc']#R U R' U' R' F R2 U R' U' F'
        break
    if oll_type==10:
        step=['R','U','Rc','U','Rc','F','R','Fc','R','U','U','Rc']#R U R' U R' F R F' R U2 R'
        break
    if oll_type==13:
        step=['F','U','R','Uc','R','R','Fc','R','U','R','Uc','Rc']#F U R U' R2 F' R U R U' R'
        break
    if oll_type==13:
        step=['F','U','R','Uc','R','R','Fc','R','U','R','Uc','Rc']#F U R U' R2 F' R U R U' R'
        break
    if oll_type==17:
        step=['R','U','Rc','U','Rc','F','R','Fc','U','U','Rc','F','R','Fc'] #R U R' U R' F R F' U2 R' F R F'
        break
    if oll_type==26:
        step=['R','U', 'U', 'Rc', 'Uc','R' ,'Uc' ,'Rc'] #R U2 R' U' R U' R'
        break
    if oll_type==44:
        step=['F','U', 'R', 'Uc', 'Rc','Fc'] #F U R U' R' F'
        break
    if oll_type==57:
        step=['R','U', 'Rc', 'Uc', 'Rc','L','F','R','Fc','Lc'] #R U R' U' R' L F R F' L'
        break

#----------------------top side-----------------------PLL1-21
#https://maru.tw/oll-pll/
pll_type=1#just for test
while(True):
    if pll_type==1 : #top side mid trangle transformer PLL01
        step=['R','R', 'U', 'R', 'U',' Rc' ,'Uc' ,'Rc' ,'Uc' ,'Rc',' U','Rc'] #R2 U R U R' U' R' U' R' U R'
    elif pll_type==2:#top side mid trangle transformer PLL02
        step=['R','Uc',' R',' U',' R',' U','R',' Uc',' Rc',' Ub' 'R','R'] #R U’ R U R U R U’ R’ U’ R2
    elif pll_type==3:#top side angle trangle transformer PLL03
        step=['R',' Bc' ,'R', 'F','F' ,'Rc' ,'B',' R', 'F','F','R','R'] #R B' R F2 R' B R F2 R2
    elif pll_type==4:#top side angle trangle transformer PLL04
        step=['R',' R' ,'F' ,'F','Rc' ,'Bc' ,'R',' F', 'F','Rc','B','Rc'] # R2 F2 R' B' R F2 R' B R'
    elif pll_type==5:#top side mid Z transformer PLL05
        step=['Rc',' Uc' ,'R' ,'Uc','R' ,'U' ,'R',' Uc', 'Rc','U','R','U','R','R','Uc','Rc','U','U'] # R' U' R U' R U R U' R' U R U R2 U' R' U2
    elif pll_type==6:#top side mid H transformer PLL06
        step=['R',' R' ,'U' ,'U','R' ,'R' ,'U',' U', 'R','R','Uc','R','R','U','U','R','R','U','U','R','R','U'] # R2 U2 R2 U2 R2 U' R2 U2 R2 U2 R2 U
    elif pll_type==7:
        step=['Uc','R','U','Rc','U','Rc','Uc','R','Fc','R','U','Rc','Uc','Rc','F','R','R','Uc','R','R','U','R']#U' (R U R' U) (R' U' R F') (R U R' U') (R' F R2 U' R2' U R)
    elif pll_type==8:
        step=['R','U','Rc','Uc','Rc','F','R','R','Uc','Rc','Uc','R','U','Rc','Fc']#R U R' U' R' F R2 U' R' U' R U R' F'
    elif pll_type==9:
        step=['Rc','U','Rc','Uc','Bc','Rc','B','B','Uc','Bc','U','Bc','R','B','R']#R' U R' U' B' R' B2 U' B' U B' R B R
    elif pll_type==10:
        step=['R''Uc','Fc','R','U','Rc','Uc','Rc','F','R','R','Uc','Rc','Uc','R','U','Rc','U','R']#R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R
    elif pll_type==11:
        step=['Rc','U','U','R','U','U','Rc','F','R','U','Rc','Uc','Rc','Fc','R','R','Uc']#R' U2 R U2 R' F R U R' U' R' F' R2 U'
    elif pll_type==12:
        step=['R','U','U','Rc','U','U','R','Bc','Rc','Uc','R','U','R','B','R','R','U']#R U2 R' U2 R B' R' U' R U R B R2 U
    elif pll_type==13:
        step=['R','U','U','Rc','Uc','R','U','U','Lc','U','Rc','Uc','L']#R U2 R' U' R U2 L' U R' U' L
    elif pll_type==14:
        step=['Rc','U','U','R','U','Rc','U','U','L','Uc','R','U','Lc']#R' U2 R U R' U2 L U' R U L'
    elif pll_type==15:
        step=['F','Rc','Fc','R','U','R','Uc','Rc','F','R','Uc','Rc','U','R','U','Rc','Fc']#F R' F' R U R U' R' F R U' R' U R U R' F'
    elif pll_type==19:
        step=['L','L','F','F','Lc','U','U','Lc','U','U','L','Fc','Lc','Uc','L','U','L','Fc','L','L']#L2 F2 L' U2 L' U2 L F' (L' U' L U) L F' L2
    elif pll_type==20:
        step=['Rc','U','R','Uc','Rc','Fc','Uc','F','R','U','Rc','F','Rc','Fc','R','Uc','R']#R' U R U' R' F' U' F R U R' F R' F' R U' R
    elif pll_type==21:
        step=['L','Uc','R','U','U','Lc','U','Rc','L','Uc','R','U','U','Lc','U','Rc','Uc']#L U' R U2 L' U R' L U' R U2 L' U R' U'
        break




rotate(step)