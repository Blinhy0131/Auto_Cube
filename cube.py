# UTF-8

import black
import cv2
import numpy as np
import math



def front_turn(data):
    #順時鐘
    ram_1=data[0][2][0]
    data[0][2][0]=data[5][2][2]
    data[5][2][2]=data[2][0][2]
    data[2][0][2]=data[3][0][0]
    data[3][0][0]=ram_1

    ram_2=data[0][2][2]
    data[0][2][2]=data[5][0][2]
    data[5][0][2]=data[2][0][0]
    data[2][0][0]=data[3][2][0]
    data[3][2][0]=ram_2

    ram_3=data[0][2][1]
    data[0][2][1]=data[5][1][2]
    data[5][1][2]=data[2][0][1]
    data[2][0][1]=data[3][1][0]
    data[3][1][0]=ram_3

    ram_4=data[1][0][0]
    data[1][0][0]=data[1][2][0]
    data[1][2][0]=data[1][2][2]
    data[1][2][2]=data[1][0][2]
    data[1][0][2]=ram_4

    ram_5=data[1][0][1]
    data[1][0][1]=data[1][1][0]
    data[1][1][0]=data[1][2][1]
    data[1][2][1]=data[1][1][2]
    data[1][1][2]=ram_5    
    
    return(data)

def back_turn(data):
    #順
    ram_1=data[0][0][0]
    data[0][0][0]=data[3][0][2]
    data[3][0][2]=data[2][2][2]
    data[2][2][2]=data[5][2][0]
    data[5][2][0]=ram_1

    ram_2=data[0][0][2]
    data[0][0][2]=data[3][2][2]
    data[3][2][2]=data[2][2][0]
    data[2][2][0]=data[5][0][0]
    data[5][0][0]=ram_2

    ram_3=data[0][0][1]
    data[0][0][1]=data[3][1][2]
    data[3][1][2]=data[2][2][1]
    data[2][2][1]=data[5][1][0]
    data[5][1][0]=ram_3

    ram_4=data[4][0][0]
    data[4][0][0]=data[4][2][0]
    data[4][2][0]=data[4][2][2]
    data[4][2][2]=data[4][0][2]
    data[4][0][2]=ram_4

    ram_5=data[4][0][1]
    data[4][0][1]=data[4][1][0]
    data[4][1][0]=data[4][2][1]
    data[4][2][1]=data[4][1][2]
    data[4][1][2]=ram_5    
    
    return(data)

def left_turn(data):
    ram_1=data[0][0][0]
    data[0][0][0]=data[4][2][2]
    data[4][2][2]=data[2][0][0]
    data[2][0][0]=data[1][0][0]
    data[1][0][0]=ram_1

    ram_2=data[0][2][0]
    data[0][2][0]=data[4][0][2]
    data[4][0][2]=data[2][2][0]
    data[2][2][0]=data[1][2][0]
    data[1][2][0]=ram_2

    ram_3=data[0][1][0]
    data[0][1][0]=data[4][1][2]
    data[4][1][2]=data[2][1][0]
    data[2][1][0]=data[1][1][0]
    data[1][1][0]=ram_3

    ram_4=data[5][0][0]
    data[5][0][0]=data[5][2][0]
    data[5][2][0]=data[5][2][2]
    data[5][2][2]=data[5][0][2]
    data[5][0][2]=ram_4

    ram_5=data[5][0][1]
    data[5][0][1]=data[5][1][0]
    data[5][1][0]=data[5][2][1]
    data[5][2][1]=data[5][1][2]
    data[5][1][2]=ram_5

    return(data)

def right_turn(data):
    ram_1=data[0][0][2]
    data[0][0][2]=data[1][0][2]
    data[1][0][2]=data[2][0][2]
    data[2][0][2]=data[4][2][0]
    data[4][2][0]=ram_1

    ram_2=data[0][2][2]
    data[0][2][2]=data[1][2][2]
    data[1][2][2]=data[2][2][2]
    data[2][2][2]=data[4][0][0]
    data[4][0][0]=ram_2

    ram_3=data[0][1][2]
    data[0][1][2]=data[1][1][2]
    data[1][1][2]=data[2][1][2]
    data[2][1][2]=data[4][1][0]
    data[4][1][0]=ram_3

    ram_4=data[3][0][0]
    data[3][0][0]=data[3][2][0]
    data[3][2][0]=data[3][2][2]
    data[3][2][2]=data[3][0][2]
    data[3][0][2]=ram_4

    ram_5=data[3][0][1]
    data[3][0][1]=data[3][1][0]
    data[3][1][0]=data[3][2][1]
    data[3][2][1]=data[3][1][2]
    data[3][1][2]=ram_5

    return(data)

def up_turn(data):

    ram_1=data[1][0]
    data[1][0]=data[3][0]
    data[3][0]=data[4][0]
    data[4][0]=data[5][0]
    data[5][0]=ram_1

    ram_4=data[0][0][0]
    data[0][0][0]=data[0][2][0]
    data[0][2][0]=data[0][2][2]
    data[0][2][2]=data[0][0][2]
    data[0][0][2]=ram_4

    ram_5=data[0][0][1]
    data[0][0][1]=data[0][1][0]
    data[0][1][0]=data[0][2][1]
    data[0][2][1]=data[0][1][2]
    data[0][1][2]=ram_5


    return(data)

def down_turn(data):
    
    ram_1=data[1][2]
    data[1][2]=data[5][2]
    data[5][2]=data[4][2]
    data[4][2]=data[3][2]
    data[3][2]=ram_1


    ram_2=data[2][0][0]
    data[2][0][0]=data[2][2][0]
    data[2][2][0]=data[2][2][2]
    data[2][2][2]=data[2][0][2]
    data[2][0][2]=ram_2

    ram_3=data[2][0][1]
    data[2][0][1]=data[2][1][0]
    data[2][1][0]=data[2][2][1]
    data[2][2][1]=data[2][1][2]
    data[2][1][2]=ram_3


    return(data)

def print_cube(color_data,img):
    
    #畫出方塊的展開圖

    for i in range(6):
        if i<2:
            x_base=100
        else:
            x_base=100+(i-2)*60
        
        if i==0 or i==2:
            y_base=100+(i-1)*60
        else:
            y_base=100
        
        for x in range(3):
            for y in range (3):
                x_start=x_base+x*20
                y_start=y_base+y*20
                x_end=x_start+15
                y_end=y_start+15
                cv2.rectangle(img, (x_start, y_start), (x_end, y_end), color_data[i][y][x] , -1)
    return(img)

def find_color(rgb):
#找出像素的HSV值 以判斷顏色 NOTE 可能需要改變S的判斷大小
    b=rgb[0]
    g=rgb[1]
    r=rgb[2]
    
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    # v = mx*100

    
    if s<30:
        color= [255,255,255] #white
    elif h<15 or h>=300:
        color=[0,0,255] #red
    elif h>=15 and h<45 :
        color=[0,128,255] #orange
    elif h>=45 and h<75 :
        color=[0,255,255] #yello
    elif h>=75 and h<180:
        color=[0,255,0] #green
    elif h>=180 and h<300:
        color=[255,0,0] #blue
    return color

def hsv2rgb(data_in):
    #目前沒用到
    h = float(data_in[0])
    s = float(data_in[1])
    v = float(data_in[2])
    if s == 0.0: v*=255;  data= [v, v, v]
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: data= [p, t, v]
    if i == 1: data= [p, v, q]
    if i == 2: data= [t, v, p]
    if i == 3: data= [v, q, p]
    if i == 4: data= [v, p, t]
    if i == 5: data= [q, p, v]
    return data

###main start###

cap = cv2.VideoCapture(0)#開啟相機
face_count=0 #介面紀錄

black_BGR=[0,0,0]
red_BGR=[0,0,255]
blue_BGR=[255,0,0]
white_BGR=[255,255,255]
yello_BGR=[0,255,255]
green_BGR=[0,255,0]
orange_GBR=[0,128,255]

up=0
front=1
down=2
right=3
back=4
left=5

#BGR color
#此為整個方塊的顏色配置
# [top_left],[topmid],[top_right] ,   [left] , [center], [right] ,[bottom_left],[bottom_mid],[botto_right]



cube_color_data=[[[black_BGR , black_BGR , black_BGR]  ,  [black_BGR , black_BGR , black_BGR]   ,  [black_BGR , black_BGR , black_BGR] ],#up
                [[black_BGR , black_BGR , black_BGR]  ,  [black_BGR , black_BGR , black_BGR]   ,  [black_BGR , black_BGR , black_BGR] ], #frount
                [[black_BGR , black_BGR , black_BGR]  ,  [black_BGR , black_BGR , black_BGR]   ,  [black_BGR , black_BGR , black_BGR] ],#down
                [[black_BGR , black_BGR , black_BGR]  ,  [black_BGR , black_BGR , black_BGR]   ,  [black_BGR , black_BGR , black_BGR] ],#right
                [[black_BGR , black_BGR , black_BGR]  ,  [black_BGR , black_BGR , black_BGR]   ,  [black_BGR , black_BGR , black_BGR] ],#back
                [[black_BGR , black_BGR , black_BGR]  ,  [black_BGR , black_BGR , black_BGR]   ,  [black_BGR , black_BGR , black_BGR] ]]#left
               
'''
cube_color_data=[[[red_BGR , red_BGR , red_BGR]  ,  [red_BGR , red_BGR , red_BGR]   ,  [red_BGR , red_BGR , red_BGR] ],#up
                [[yello_BGR , yello_BGR , yello_BGR]  ,  [yello_BGR , yello_BGR , yello_BGR]   ,  [yello_BGR , yello_BGR , yello_BGR] ], #frount
                [[orange_GBR , orange_GBR , orange_GBR]  ,  [orange_GBR , orange_GBR , orange_GBR]   ,  [orange_GBR , orange_GBR , orange_GBR] ],#down
                [[blue_BGR , blue_BGR , blue_BGR]  ,  [blue_BGR , blue_BGR , blue_BGR]   ,  [blue_BGR , blue_BGR , blue_BGR] ],#right
                [[white_BGR , white_BGR , white_BGR]  ,  [white_BGR , white_BGR , white_BGR]   ,  [white_BGR , white_BGR , white_BGR] ],#back
                [[green_BGR , green_BGR , green_BGR]  ,  [green_BGR , green_BGR , green_BGR]   ,  [green_BGR , green_BGR , green_BGR] ]]#left
                #測試用 完整顏色 '''
'''
cube_color_data=[[[[255, 0, 0], [255, 0, 0], [0, 255, 0]], [[255, 0, 0], [0, 255, 0], [0, 128, 255]], [[255, 0, 0], [255, 255, 255], [255, 255, 255]]], 
                [[[0, 255, 255], [0, 128, 255], [0, 255, 0]], [[0, 255, 255], [255, 255, 255], [0, 255, 255]], [[255, 255, 255], [0, 255, 255], [255, 255, 255]]], 
                [[[0, 128, 255], [0, 0, 255], [0, 128, 255]], [[0, 255, 0], [255, 0, 0], [0, 255, 0]], [[0, 128, 255], [0, 255, 0], [255, 0, 0]]], 
                [[[0, 0, 255], [0, 255, 255], [0, 255, 255]], [[255, 0, 0], [0, 128, 255], [0, 0, 255]], [[0, 255, 0], [0, 0, 255], [0, 128, 255]]], 
                [[[0, 0, 255], [0, 128, 255], [255, 255, 255]], [[255, 255, 255], [0, 255, 255], [255, 0, 0]], [[0, 255, 255], [255, 255, 255], [0, 255, 0]]], 
                [[[0, 0, 255], [0, 128, 255], [0, 0, 255]], [[255, 255, 255], [0, 0, 255], [0, 255, 0]], [[0, 255, 255], [0, 128, 255], [255, 0, 0]]]]
'''
'''
data[0]                                   | data[up]     

data[1]   data[3]    data[4]    data[5]   | data[front]   data[right]    data[back]    data[left]  

data[2]                                   | data[up]           

---------
| U U U |
| U U U |
| U U U |
---------------------------------
| F F F | R R R | B B B | L L L |
| F F F | R R R | B B B | L L L |
| F F F | R R R | B B B | L L L |
---------------------------------
| D D D |
| D D D |
| D D D |
---------

'''



#相機判斷顏色
cam_on=True

while(cam_on):
    ret,img = cap.read()#捕獲一幀影象


    grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#改成線型(邊緣輪廓)
    blurredFrame = cv2.blur(grayFrame, (3, 3))
    canny = cv2.Canny(blurredFrame, 30, 150) 

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))#輪廓加粗
    dilatedFrame = cv2.dilate(canny, kernel)

    img_rgb = cv2.cvtColor(dilatedFrame, cv2.COLOR_BGRA2RGB)  # 色彩空間轉換爲RGB

    

    top_left =  list(map(int,img[125,175]))
    top_mid =  list(map(int,img[125,275]))
    top_right =  list(map(int,img[125,375]))
    left= list(map(int,img[225,175]))
    center=list(map(int,img[225,275]))
    right=list(map(int,img[225,375]))
    bottom_left=list(map(int,img[325,175]))
    bottom_mid=list(map(int,img[325,275]))
    bottom_right=list(map(int,img[325,375]))

    cv2.rectangle(img_rgb, (150, 100), (200, 150), top_left , 10)
    cv2.rectangle(img_rgb, (250, 100), (300, 150), top_mid, 10)
    cv2.rectangle(img_rgb, (350, 100), (400, 150), top_right, 10)
    cv2.rectangle(img_rgb, (150, 200), (200, 250), left, 10)
    cv2.rectangle(img_rgb, (250, 200), (300, 250), center, 10)
    cv2.rectangle(img_rgb, (350, 200), (400, 250), right, 10)
    cv2.rectangle(img_rgb, (150, 300), (200, 350), bottom_left, 10)
    cv2.rectangle(img_rgb, (250, 300), (300, 350), bottom_mid, 10)
    cv2.rectangle(img_rgb, (350, 300), (400, 350), bottom_right, 10)



    control=cv2.waitKey(1)

    if control== ord('z'):
        #空白鍵
        #紀錄顏色
        if face_count<6:
            #cube_color_data[face_count]=[[top_left,top_mid,top_right],[left,center,right],[bottom_left,bottom_mid,bottom_right]]

            cube_color_data[face_count][0][0]=find_color(top_left)
            cube_color_data[face_count][0][1]=find_color(top_mid)
            cube_color_data[face_count][0][2]=find_color(top_right)
            cube_color_data[face_count][1][0]=find_color(left)
            cube_color_data[face_count][1][1]=find_color(center)
            cube_color_data[face_count][1][2]=find_color(right)
            cube_color_data[face_count][2][0]=find_color(bottom_left)
            cube_color_data[face_count][2][1]=find_color(bottom_mid)
            cube_color_data[face_count][2][2]=find_color(bottom_right)

            face_count=face_count+1
    if control==8:
        #backspace
        if face_count!=0:
            face_count=face_count-1
            cube_color_data[face_count]=[[black_BGR , black_BGR , black_BGR],[black_BGR , black_BGR , black_BGR], [black_BGR , black_BGR , black_BGR]]
            

    if control==13 :
        cam_on=False

    

    img=print_cube(cube_color_data,img)

    #cv2.rectangle(img_rgb, (174, 124), (176, 126), (0, 255, 0), 1)

    image = np.concatenate([img_rgb, img], axis=1) #合併圖像
    cv2.imshow('img', image)
    #print(cube_color_data[0][0][0])



    #cv2.imshow('frame',frame)
    #判斷按鍵，如果按鍵為q，退出迴圈
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    if cv2.waitKey(1) ==27:
        # ESC key
        break

cap.release()#關閉相機
cv2.destroyAllWindows()#關閉視窗
#print(cube_color_data)

#手動控制 
while(True):
    control=cv2.waitKey(1)
    if control == ord('a'):
        cube_color_data=left_turn(cube_color_data)
    if control == ord('d'):
        cube_color_data=right_turn(cube_color_data)
    if control == ord('w'):
        cube_color_data=up_turn(cube_color_data)
    if control == ord('x'):
        cube_color_data=down_turn(cube_color_data)
    if control == ord('s'):
        cube_color_data=front_turn(cube_color_data)
    if control == ord('z'):
        cube_color_data=back_turn(cube_color_data)


    img = np.zeros((512,512,3), np.uint8)
    img=print_cube(cube_color_data,img)
    cv2.imshow('img2', img)

    if cv2.waitKey(1) ==27:
        # ESC key
        break


'''while(True):
    while cube_color_data[back][0][1] !=cube_color_data[back][1][0]!=cube_color_data[back][2][1]!=cube_color_data[back][0][1]!=cube_color_data[back][1][2]!=[back][1][1]:
        if ((cube_color_data[front]==black_BGR).any()):
            if
            else:
                cube_color_data=up_turn(cube_color_data)'''




cv2.destroyAllWindows()#關閉視窗
