import maya.cmds as cmds
import random


SnowmanBottom = 3.0
SnowmanMiddle = 2.0
SnowmanTop = 1.0

addHat = True
randomizePosition = False


bottom_sphere = cmds.polySphere(r=SnowmanBottom, name="BottomSphere")[0]
cmds.move(0, SnowmanBottom, 0, bottom_sphere)


middle_sphere = cmds.polySphere(r=SnowmanMiddle, name="MiddleSphere")[0]
cmds.move(0, SnowmanBottom * 2 + SnowmanMiddle, 0, middle_sphere)


top_sphere = cmds.polySphere(r=SnowmanTop, name="TopSphere")[0]
cmds.move(0, SnowmanBottom * 2 + SnowmanMiddle * 2 + SnowmanTop, 0, top_sphere)


if addHat:
    hat = cmds.polyCone(r=0.5, h=1, name="Snowman_Hat")[0]
    cmds.move(0, SnowmanBottom * 2 + SnowmanMiddle * 2 + SnowmanTop * 2 + 0.5, 0, hat)


eye_distance = 0.3  
eye_height = SnowmanBottom * 2 + SnowmanMiddle * 2 + SnowmanTop * 1  
eye_offset = SnowmanTop + 0 
eye_size = 0.2  

left_eye = cmds.polySphere(r=eye_size, name="LeftEye")[0]
cmds.move(-eye_distance, eye_height, eye_offset, left_eye)

right_eye = cmds.polySphere(r=eye_size, name="RightEye")[0]
cmds.move(eye_distance, eye_height, eye_offset, right_eye)


button_size = 0.15  


button1_offset_z = 1.9
button2_offset_z = 2
button3_offset_z = 1.9

button1 = cmds.polySphere(r=button_size, name="Button1")[0]
cmds.move(0, SnowmanBottom * 2 + SnowmanMiddle - 0.5, button1_offset_z, button1)

button2 = cmds.polySphere(r=button_size, name="Button2")[0]
cmds.move(0, SnowmanBottom * 2 + SnowmanMiddle, button2_offset_z, button2)

button3 = cmds.polySphere(r=button_size, name="Button3")[0]
cmds.move(0, SnowmanBottom * 2 + SnowmanMiddle + 0.5, button3_offset_z, button3)


if randomizePosition:
    randX = random.uniform(-5, 5)
    cmds.move(randX, 0, 0, bottom_sphere)
    cmds.move(randX, SnowmanBottom * 1 + SnowmanMiddle, 0, middle_sphere)
    cmds.move(randX, SnowmanBottom * 1 + SnowmanMiddle * 2 + SnowmanTop, 0, top_sphere)
    cmds.move(randX - eye_distance, eye_height, eye_offset, left_eye)
    cmds.move(randX + eye_distance, eye_height, eye_offset, right_eye)
    cmds.move(randX, SnowmanBottom * 2 + SnowmanMiddle - 0.5, button1_offset_z, button1)
    cmds.move(randX, SnowmanBottom * 2 + SnowmanMiddle, button2_offset_z, button2)
    cmds.move(randX, SnowmanBottom * 2 + SnowmanMiddle + 0.5, button3_offset_z, button3)
