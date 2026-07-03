from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create()
Pos = mc.player.getTilePos()
x=Pos.x
y=Pos.y
z=Pos.z

# a=0
# for i in range(4):
    # mc.setBlock(x,y,z+a,35,8)
    # mc.setBlock(x+1,y,z+a,35,7)
    # mc.setBlock(x+2,y,z+a,35,8)
    # mc.setBlock(x+3,y,z+a,35,7)
    # mc.setBlock(x+4,y,z+a,35,8)
    # mc.setBlock(x+5,y,z+a,35,7)
    # mc.setBlock(x+6,y,z+a,35,8)
    # mc.setBlock(x+7,y,z+a,35,7)
    # l=0
    # for k in range (4):
    #     mc.setBlock(x+l, y, z + a, 35, 8)
    #     mc.setBlock(x+l+1,y, z + a, 35, 7)
    #     l=l+2
    # a=a+1
    # l=0
    # mc.setBlock(x,y,z+a,35,7)
    # mc.setBlock(x+1,y,z+a,35,8)
    # mc.setBlock(x+2,y,z+a,35,7)
    # mc.setBlock(x+3,y,z+a,35,8)
    # mc.setBlock(x+4,y,z+a,35,7)
    # mc.setBlock(x+5,y,z+a,35,8)
    # mc.setBlock(x+6,y,z+a,35,7)
    # mc.setBlock(x+7,y,z+a,35,8)
    # a=a+1
# mc.setBlock(x,y,z,35,7)
# mc.setBlock(x+1,y,z,35,7)
# mc.setBlock(x+2,y,z,35,7)
# mc.setBlock(x+3,y,z,35,7)
# mc.setBlock(x+1,y+1,z,35,7)
# mc.setBlock(x+2,y+1,z,35,7)
# mc.setBlock(x+3,y+1,z,35,7)
# mc.setBlock(x+2,y+2,z,35,7)
# mc.setBlock(x+3,y+2,z,35,7)
# mc.setBlock(x+3,y+3,z,35,7)
a=10
b=0
for i in range (a,0,-1):
    for k in range(i):
        print(i,k)
        mc.setBlock(x+k,y+b,z,35,7)
    b+=1

    #for i in range(4):
    #     mc.setBlock(x+i,y,z,35,7)
    # for i in range(3):
    #     mc.setBlock(x + i, y+1, z, 35, 7)
    # for i in range(2):
    #     mc.setBlock(x + i, y+2, z, 35, 7)
    # for i in range(1):
    #     mc.setBlock(x + i, y + 3, z, 35, 7)
