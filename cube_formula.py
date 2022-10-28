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

def correct_check(side,data):
    print('do something')
    return('uncorrect_nem')

data=['cube_color_data']

#need 2 find the front side
#but how 2 find

#----------------------bottom side -----------------------
    #the first step need to find the 4 side of the bottom side
    #1.know the bottom color
    #2.find the color of the side
    #3.how 2 rotate?

    #find the bottom side color
bottom_color=data[2][1][1] #1.
front_color=data[1][1][1]
top_color=data[0][1][1]
right_color=data[3][1][1]
back_color=data[4][1][1]
left_color=data[5][1][1]

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
    if oll_type==2:
        step=['F','R', 'U', 'Rc', 'Uc',' Fc' ,'B' ,'U' ,'L' ,'Uc',' Lc','Bc'] #F R U R' U' F' B U L U' L' B'
    if oll_type==3:
        step=['Lc','R','R','B','Rc','B','L','U','U','Lc','B','Rc','L']#L' R2 B R' B L U2 L' B R' L
    if oll_type==4:
        step=['R','L','L','Bc','L','Bc','Rc','U','U','R','Bc','Rc','L']#R L2 B' L B' R' U2 R B' R' L
    if oll_type==9:
        step=['R','U','Rc','Uc','Rc','F','R','R','U','Rc','Uc','Fc']#R U R' U' R' F R2 U R' U' F'
    if oll_type==10:
        step=['R','U','Rc','U','Rc','F','R','Fc','R','U','U','Rc']#R U R' U R' F R F' R U2 R'
    if oll_type==13:
        step=['F','U','R','Uc','R','R','Fc','R','U','R','Uc','Rc']#F U R U' R2 F' R U R U' R'
    if oll_type==13:
        step=['F','U','R','Uc','R','R','Fc','R','U','R','Uc','Rc']#F U R U' R2 F' R U R U' R'
    if oll_type==17:
        step=['R','U','Rc','U','Rc','F','R','Fc','U','U','Rc','F','R','Fc'] #R U R' U R' F R F' U2 R' F R F'
    if oll_type==26:
        step=['R','U', 'U', 'Rc', 'Uc','R' ,'Uc' ,'Rc'] #R U2 R' U' R U' R'
    if oll_type==44:
        step=['F','U', 'R', 'Uc', 'Rc','Fc'] #F U R U' R' F'
    if oll_type==57:
        step=['R','U', 'Rc', 'Uc', 'Rc','L','F','R','Fc','Lc'] #R U R' U' R' L F R F' L'

#----------------------top side-----------------------PLL1-21
#https://maru.tw/oll-pll/
pll_type=0#just for test


#side isnt correct 3 PLL1,2
#side isnt correct 2 and angle is correct 2 PLL8-12 20 21
#side isnt correct 4 PLL5,6
#angle isnt correct 4 PLL7
#angle isnt correct 3 PLL3,4

#know check the top corner 
#correct_check(x,y)
#x=1 mean side x=2 ;mean angle
angle_uncorrect_nem=correct_check(2,data)
side_uncorrect_nem=correct_check(1,data)
if angle_uncorrect_nem==4:
    pll_type=7
    #find the front face
    
    
if angle_uncorrect_nem==3:
    pll_type=3
    pll_type=4
    
    
if side_uncorrect_nem==4:
    pll_type=5,6


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
    #NO PLL16-19 
    elif pll_type==20:
        step=['Rc','U','R','Uc','Rc','Fc','Uc','F','R','U','Rc','F','Rc','Fc','R','Uc','R']#R' U R U' R' F' U' F R U R' F R' F' R U' R
    elif pll_type==21:
        step=['L','Uc','R','U','U','Lc','U','Rc','L','Uc','R','U','U','Lc','U','Rc','Uc']#L U' R U2 L' U R' L U' R U2 L' U R' U'



rotate(step)