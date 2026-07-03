from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
Pos = mc.player.getPos()
x = 100
y = 1000
z = 100
#mc.player.setTilePos(x,y,z,)


print (Pos)

x = 100
y = -12
z = 100










mc=Minecraft.create()
pos=mc.player.getTilePos()
print(pos)

print ('teleport')
time.sleep(10)
x = -61
y = 0
z = -153
mc.player.setPos (x,y,z)


time.sleep(10)

x1=-41
y1=19
z1=-78

time.sleep(10)
mc.player.setPos (x,y,z)

x2=-47
y2=3
z2=-44
time.sleep(10)
mc.player.setPos (x,y,z)
#залізний №42 золотий №41 алмазний №57
