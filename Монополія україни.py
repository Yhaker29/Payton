import random
# -67,2,-24
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
Pos = mc.player.getTilePos()

x=-76
y=17
z=-52
print(Pos)
# mc.player.setTilePos(x,y,z)
#
# Points2=0
# Points=0
# mc.setBlocks(x,y,z,x,y,z+26,216)
# mc.setBlocks(x+2,y,z,x+2,y,z+26,216)
# mc.setBlock(x+2,y+1,z,57)
# mc.setBlock(x,y+1,z,41)
#
# while True:
#     a=input('(PLAYER1)Ви готові кинути кубик?')
#     if a==('Так')  or a==('так'):
#         mc.setBlocks(x,y+1,z,x,y+1,z+26,0)
#         namber=random.randint(1,6)
#         print(namber)
#         Points+=namber
#         mc.setBlock(x,y+1,z+Points,41)
#         print('Ви знаходитесь на клітинці', Points, )
#         mc.postToChat('Ви знаходитесь на клітинці', Points, )
#
#         if Points == 26 or Points >= 27:
#             print('(PLAYER1)Перемога! У тебе', Points, 'балів!')
#             mc.postToChat('(PLAYER1)Перемога! У тебе', Points, 'балів!')
#             break
#
#         a = input('(PLAYER2)Ви готові кинути кубик?')
#     if a == ('Так') or a == ('так'):
#         mc.setBlocks(x+2,y+1,z,x+2,y+1,z+26,0)
#         namber2 = random.randint(1, 6)
#         print(namber2)
#         Points2 += namber2
#         mc.setBlock(x+2,y+1,z+Points2,57)
#         print ('Ви знаходитесь на клітинці',Points2,)
#         mc.postToChat('Ви знаходитесь на клітинці',Points2,)
#     if Points2==26 or Points2>=27:
#         print('(PLAYER2)Перемога! У тебе',Points2,'балів!')
#         mc.postToChat('(PLAYER2)Перемога! У тебе',Points2,'балів!')
#         break
#     if a==('Ні')  or a==('ні'):
#         print ('То йди гуляй!!!')
mc.setBlock(x,y,z,1)
mc.setBlock(x+1,y+1,z,1)
mc.setBlock(x+2,y+2,z,1)
mc.setBlock(x+3,y+3,z,1)
mc.setBlock(x+4,y+4,z,1)
mc.setBlock(x+5,y+5,z,1)
mc.setBlock(x+6,y+5,z,1)
mc.setBlock(x+7,y+5,z,1)
mc.setBlock(x+8,y+5,z,1)
mc.setBlock(x+9,y+5,z,1)
mc.setBlock(x+10,y+4,z,1)
mc.setBlock(x+11,y+3,z,1)
mc.setBlock(x+12,y+2,z,1)
mc.setBlock(x+13,y+1,z,1)
mc.setBlock(x+14,y,z,1)
mc.setBlock(x,y,z+1,1)
mc.setBlock(x+1,y+1,z+1,1)
mc.setBlock(x+2,y+2,z+1,1)
mc.setBlock(x+3,y+3,z+1,1)
mc.setBlock(x+4,y+4,z+1,1)
mc.setBlock(x+5,y+5,z+1,1)
mc.setBlock(x+6,y+5,z+1,1)
mc.setBlock(x+7,y+5,z+1,1)
mc.setBlock(x+8,y+5,z+1,1)
mc.setBlock(x+9,y+5,z+1,1)
mc.setBlock(x+10,y+4,z+1,1)
mc.setBlock(x+11,y+3,z+1,1)
mc.setBlock(x+12,y+2,z+1,1)
mc.setBlock(x+13,y+1,z+1,1)
mc.setBlock(x+14,y,z+1,1)
mc.setBlock(x,y,z+2,1)
mc.setBlock(x+1,y+1,z+2,1)
mc.setBlock(x+2,y+2,z+2,1)
mc.setBlock(x+3,y+3,z+2,1)
mc.setBlock(x+4,y+4,z+2,1)
mc.setBlock(x+5,y+5,z+2,1)
mc.setBlock(x+6,y+5,z+2,1)
mc.setBlock(x+7,y+5,z+2,1)
mc.setBlock(x+8,y+5,z+2,1)
mc.setBlock(x+9,y+5,z+2,1)
mc.setBlock(x+10,y+4,z+2,1)
mc.setBlock(x+11,y+3,z+2,1)
mc.setBlock(x+12,y+2,z+2,1)
mc.setBlock(x+13,y+1,z+2,1)
mc.setBlock(x+14,y,z+2,1)
mc.setBlock(x,y,z+3,1)
mc.setBlock(x+1,y+1,z+3,1)
mc.setBlock(x+2,y+2,z+3,1)
mc.setBlock(x+3,y+3,z+3,1)
mc.setBlock(x+4,y+4,z+3,1)
mc.setBlock(x+5,y+5,z+3,1)
mc.setBlock(x+6,y+5,z+3,1)
mc.setBlock(x+7,y+5,z+3,1)
mc.setBlock(x+8,y+5,z+3,1)
mc.setBlock(x+9,y+5,z+3,1)
mc.setBlock(x+10,y+4,z+3,1)
mc.setBlock(x+11,y+3,z+3,1)
mc.setBlock(x+12,y+2,z+3,1)
mc.setBlock(x+13,y+1,z+3,1)
mc.setBlock(x+14,y,z+3,1)
mc.setBlocks(x+5,y+6,z,x+5,y+9,z,1)
mc.setBlocks(x+9,y+6,z,x+9,y+9,z,1)
mc.setBlocks(x+5,y+6,z+3,x+5,y+9,z+3,1)
mc.setBlocks(x+9,y+6,z+3,x+9,y+9,z+3,1)
mc.setBlocks(x+5,y+9,z,x,y+9,z+3,1)
mc.setBlock(x+7,y+9,z+2,124)
mc.setBlock(x+7,y+10,z+2,152)
mc.setBlock(x+7,y+9,z+1,124)
mc.setBlock(x+7,y+10,z+1,152)
mc.setBlock(x+8,y+9,z+2,124)
mc.setBlock(x+8,y+10,z+2,152)
mc.setBlock(x+8,y+9,z+1,124)
mc.setBlock(x+8,y+10,z+1,152)