from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
Pos = mc.player.getPos()
x=Pos.x
y=Pos.y
z=Pos.z
for i in range(5,100,3):
    print (i)