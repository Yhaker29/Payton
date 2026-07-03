from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create()
Pos = mc.player.getTilePos()
x=Pos.x
y=Pos.y
z=Pos.z




# for i in range (10):
#     print ('привіт')
# print ('пока')
a=0
# f0or i in range (101):
# mc.setBlock(x,y,z,1)
# mc.setBlock(x+1,y+1,z,1)
# mc.setBlock(x+2,y+2,z,1)
# mc.setBlock(x+3,y+3,z,1)
# mc.setBlock(x+4,y+1,z,1)
# mc.setBlock(x+5,y+2,z,1)
# mc.setBlock(x+6,y+3,z,1)
# mc.setBlock(x+7,y+1,z,1)
# mc.setBlock(x+8,y+2,z,1)
# mc.setBlock(x+9,y+3,z,1)
# for i in range (9999):
#     mc.setBlock(x+i,y+a,z,41)
#     a+=1
#     if a==3:
#         a=0
b=0
# for i in range (10000):
#     mc.setBlock(x+a,y+b,z,35,random.randint(1,15))
#     a+=1
#     if a==5:
#         a=0
#         b+=1
for i in range (100):
    d=0
    for i in range (5):
        mc.setBlock(x+2,y+d,z+1,41)
        d+=1
    mc.setBlock(x+1,y,z,35)
    mc.setBlock(x+2,y,z,35)
    mc.setBlock(x+3,y,z,35)
    mc.setBlock(x+1,y,z+1,35)
    mc.setBlock(x+2,y,z+1,41)
    mc.setBlock(x+3,y,z+1,35)
    mc.setBlock(x+1,y,z+2,35)
    mc.setBlock(x+2,y,z+2,35)
    mc.setBlock(x+3,y,z+2,35)
    mc.setBlock(x+1,y+5,z,35)
    mc.setBlock(x+2,y+5,z,35)
    mc.setBlock(x+3,y+5,z,35)
    mc.setBlock(x+1,y+5,z+1,35)
    mc.setBlock(x+2,y+5,z+1,41)
    mc.setBlock(x+3,y+5,z+1,35)
    mc.setBlock(x+1,y+5,z+2,35)
    mc.setBlock(x+2,y+5,z+2,35)
    mc.setBlock(x+3,y+5,z+2,35)
    x=x+10
# d=0
# for i in range (5):
#     mc.setBlock(x+2,y+d,z+1,41)
#     d+=1
# mc.setBlock(x+1,y,z,35)
# mc.setBlock(x+2,y,z,35)
# mc.setBlock(x+3,y,z,35)
# mc.setBlock(x+1,y,z+1,35)
# mc.setBlock(x+2,y,z+1,41)
# mc.setBlock(x+3,y,z+1,35)
# mc.setBlock(x+1,y,z+2,35)
# mc.setBlock(x+2,y,z+2,35)
# mc.setBlock(x+3,y,z+2,35)
# mc.setBlock(x+1,y+5,z,35)
# mc.setBlock(x+2,y+5,z,35)
# mc.setBlock(x+3,y+5,z,35)
# mc.setBlock(x+1,y+5,z+1,35)
# mc.setBlock(x+2,y+5,z+1,41)
# mc.setBlock(x+3,y+5,z+1,35)
# mc.setBlock(x+1,y+5,z+2,35)
# mc.setBlock(x+2,y+5,z+2,35)
# mc.setBlock(x+3,y+5,z+2,35)
# d=0
# for i in range (5):
#     mc.setBlock(x+2,y+d,z+1,41)
#     d+=1
# x=x+10
# mc.setBlock(x+1,y,z,35)
# mc.setBlock(x+2,y,z,35)
# mc.setBlock(x+3,y,z,35)
# mc.setBlock(x+1,y,z+1,35)
# mc.setBlock(x+2,y,z+1,41)
# mc.setBlock(x+3,y,z+1,35)
# mc.setBlock(x+1,y,z+2,35)
# mc.setBlock(x+2,y,z+2,35)
# mc.setBlock(x+3,y,z+2,35)
# mc.setBlock(x+1,y+5,z,35)
# mc.setBlock(x+2,y+5,z,35)
# mc.setBlock(x+3,y+5,z,35)
# mc.setBlock(x+1,y+5,z+1,35)
# mc.setBlock(x+2,y+5,z+1,41)
# mc.setBlock(x+3,y+5,z+1,35)
# mc.setBlock(x+1,y+5,z+2,35)
# mc.setBlock(x+2,y+5,z+2,35)
# mc.setBlock(x+3,y+5,z+2,35)
#
# for i in range (5):
#     mc.setBlock(x+2,y+d,z+1,41)
#     d+=1
# x=x+10
# mc.setBlock(x+1,y,z,35)
# mc.setBlock(x+2,y,z,35)
# mc.setBlock(x+3,y,z,35)
# mc.setBlock(x+1,y,z+1,35)
# mc.setBlock(x+2,y,z+1,41)
# mc.setBlock(x+3,y,z+1,35)
# mc.setBlock(x+1,y,z+2,35)
# mc.setBlock(x+2,y,z+2,35)
# mc.setBlock(x+3,y,z+2,35)
# mc.setBlock(x+1,y+5,z,35)
# mc.setBlock(x+2,y+5,z,35)
# mc.setBlock(x+3,y+5,z,35)
# mc.setBlock(x+1,y+5,z+1,35)
# mc.setBlock(x+2,y+5,z+1,41)
# mc.setBlock(x+3,y+5,z+1,35)
# mc.setBlock(x+1,y+5,z+2,35)
# mc.setBlock(x+2,y+5,z+2,35)
# mc.setBlock(x+3,y+5,z+2,35)
