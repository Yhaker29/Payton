from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create()
Pos = mc.player.getTilePos()
x=Pos.x
y=Pos.y
z=Pos.z


# Борщ=['картопля', 'буряк', 'капусточка', 'вода','сметана','м*ясо']
# Борщ.pop(0)
# print(Борщ)
# f=[1,2,3,4,5,6,7,8]
# for i in range(0,6):
#     f.insert(i,0)
# f.insert(7,100)
# for a in range(10):
#     f.append(55)
# print(f)

mc.setBlocks(x,y,z,x,y+9,z,1)

s=0
a=[1,1,1,1,1,1,1,1,1,1]
b=41
c=0
while True:
    a[c]=b
    time.sleep(1)
    print('╰(*°▽°*)╯')
    mc.setBlock(x,y,z,a[0])
    mc.setBlock(x,y+1,z,a[1])
    mc.setBlock(x, y+2, z, a[2])
    mc.setBlock(x, y + 3, z, a[3])
    mc.setBlock(x, y+4, z, a[4])
    mc.setBlock(x, y + 5, z, a[5])
    mc.setBlock(x, y + 6, z, a[6])
    mc.setBlock(x, y + 7, z, a[7])
    mc.setBlock(x, y + 8, z, a[8])
    mc.setBlock(x, y + 9, z, a[9])
    c+=1
    if c==10:
        a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        c = 0
        s+=10
        print(str(s)+'секунд пройшло')
        mc.postToChat(str(s)+'секунд пройшло')