from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
Pos = mc.player.getPos()
x = 159
y = 32
z = 211
print (Pos)
x1 =188
y1 = 23
z1 = 182
mc.postToChat(Pos)
x2 = 100
y2 = -13
z2 = 100
mc.postToChat(Pos)
time.sleep(7)
mc.player.setPos(x,y,z)
time.sleep(7)
mc.player.setPos(x2,y2,z2)
time.sleep(7)
mc.player.setPos(x1,y1,z1)  