from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
Pos = mc.player.getTilePos()
x=Pos.x
y=Pos.y
z=Pos.z
a='n'
if a=='yes':
   mc.setBlocks(x,y,z,x+4,y+4,z+4,41)
   mc.setBlocks(x+1,y+1,z+1,x+3,y+4,z+3,9)
   print ('yes')
elif a=='no':
    mc.setBlocks(x,y,z,x+4,y+4,z+4,41)
    mc.setBlocks(x+1,y,z+1,x+3,y+3,z+3,0)
    print ('no')
else:
    mc.setBlock(x,y,z,103)
