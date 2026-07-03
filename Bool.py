from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
Pos = mc.player.getTilePos()
x=Pos.x
y=Pos.y
z=Pos.z
# a=28
# print (a>18)
# a=mc.getBlock(x,y,z)
# print(a==8)
# a=12
# b=12
# c=2000
# # print (a==b and a==c)
# # print (a>0 or b>0 or c>0)
# print(a==b or b==a  or a==c)
print (x,y,z)
x=255
y=12
z=291


# mc.setBlocks(x,y,z,x+4,y+4,z+4,41)
# mc.setBlocks(x+1,y+1,z+1,x+3,y+3,z+3,0)

# Pos = mc.player.getTilePos()
# print (y<Pos.y and y+4>Pos.y and z<Pos.z and z+4>Pos.z and x<Pos.x and x+4>Pos.x)

