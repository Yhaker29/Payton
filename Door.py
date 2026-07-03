from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
Pos = mc.player.getTilePos()
x=200
y=-59
z=319
mc.setBlock(x,y,z,41)
mc.setBlock(x,y+1,z,41)
mc.setBlock(x,y+2,z,41)
mc.setBlock(x,y+3,z,41)
mc.setBlock(x+1,y,z,41)
mc.setBlock(x+1,y+1,z,41)
mc.setBlock(x+1,y+2,z,41)
mc.setBlock(x+1,y+3,z,41)
print (Pos)
x1=200
y1=-58
z1=316
while True:
    Blok=mc.getBlock(x1,y1,z1)
    print(Blok)
    if Blok==29:
        mc.setBlock(x, y, z, 7)
        mc.setBlock(x, y + 1, z, 7)
        mc.setBlock(x, y + 2, z, 7)
        mc.setBlock(x, y + 3, z, 7)
        mc.setBlock(x + 1, y, z, 7)
        mc.setBlock(x + 1, y + 1, z, 7)
        mc.setBlock(x + 1, y + 2, z, 7)
        mc.setBlock(x + 1, y + 3, z, 7)
    if Blok==41:
        mc.setBlock(x, y, z, 41)
        mc.setBlock(x, y + 1, z, 41)
        mc.setBlock(x, y + 2, z, 41)
        mc.setBlock(x, y + 3, z, 41)
        mc.setBlock(x + 1, y, z, 41)
        mc.setBlock(x + 1, y + 1, z, 41)
        mc.setBlock(x + 1, y + 2, z, 41)
        mc.setBlock(x + 1, y + 3, z, 41)
    if Blok==216:
        mc.setBlock(x, y, z, 0)
        mc.setBlock(x, y + 1, z, 0)
        mc.setBlock(x, y + 2, z, 0)
        mc.setBlock(x, y + 3, z, 0)
        mc.setBlock(x + 1, y, z, 0)
        mc.setBlock(x + 1, y + 1, z, 0)
        mc.setBlock(x + 1, y + 2, z, 0)
        mc.setBlock(x + 1, y + 3, z, 0)
    if Blok==5:
        mc.setBlock(x, y, z, 57)
        mc.setBlock(x, y + 1, z, 57)
        mc.setBlock(x, y + 2, z, 57)
        mc.setBlock(x, y + 3, z, 57)
        mc.setBlock(x + 1, y, z, 57)
        mc.setBlock(x + 1, y + 1, z, 57)
        mc.setBlock(x + 1, y + 2, z, 57)
        mc.setBlock(x + 1, y + 3, z, 57)
    time.sleep(0.5)