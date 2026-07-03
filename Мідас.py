import random

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
Pos = mc.player.getTilePos()
x=-30
y=-15
z=-1
print(Pos)
# while True:
#     time.sleep(0.2)
#     Pos = mc.player.getPos()
#     print(Pos)
#     Block = mc.getBlock((Pos.x,Pos.y-1,Pos.z))
#     if Block!=0 and Block!=8 and Block!=9:
#         mc.setBlock(Pos.x, Pos.y-1,Pos.z, 51)
# mc.setBlocks(x,y,z,x+9,y,z+9,35)
# while True:
#     Pos = mc.player.getTilePos()
#     if Pos.x>=x and Pos.x<=x+9 and Pos.z>=z and Pos.z<=z+9 and Pos.y-1==y:
#         a=random.randint(0,15)
#         mc.setBlocks(x,y,z,x+9,y,z+9,35,a)
#         time.sleep(1)
# св=4
# xrandom=random.randint(1,4)
# zrandom=random.randint(1,4)
# mc.setBlock(x+xrandom,y,z+zrandom,46)
# xrandom2=random.randint(-4,-1)
# zrandom2=random.randint(-4,-1)
# mc.setBlock(x+xrandom2,y,z+zrandom2,46)
# xrandom3=random.randint(-4,4)
# zrandom3=random.randint(-4,4)
# mc.setBlock(x+xrandom3,y,z+zrandom3,46)
# while True:
#         Pos = mc.player.getTilePos()
#         Block = mc.getBlock((Pos.x, Pos.y - 1, Pos.z))
#         if Block==46:
#             св=св-1
#             print(св)
#             mc.postToChat(св)
#             if св==0:
#                 print('BOOOOOOOOOOOOOOOOOOOOOOOOOOM')
#                 mc.postToChat('BOOOOOOOOOOOOOOOOOOOOOOOOOOM')
#                 mc.setBlocks(x-1,y-1,z-1,x+3,y+3,z+3,0)
#                 break
#         else:
#             св=4
#         time.sleep(1)
red_block=14
blue_block=11
current_block=blue_block
mc.setBlocks(x,y,z,x+6,y,z+6,41)
mc.setBlock(x+1,y,z+1,216) #1
mc.setBlock(x+1,y,z+3,216) #2
mc.setBlock(x+1,y,z+5,216) #3
mc.setBlock(x+3,y,z+1,216) #4
mc.setBlock(x+3,y,z+3,216) #5
mc.setBlock(x+3,y,z+5,216) #6
mc.setBlock(x+5,y,z+1,216) #7
mc.setBlock(x+5,y,z+3,216) #8
mc.setBlock(x+5,y,z+5,216) #9
cell1=0
cell2=0
cell3=0
cell4=0
cell5=0
cell6=0
cell7=0
cell8=0
cell9=0

winer=0
while True:
    a=int(input('Ведіть число від 1-9'))
    if a ==1 and cell1==0:
        mc.setBlock(x + 1, y, z + 1, 35,current_block)
        cell1  =current_block
    if a ==2 and cell2==0:
        mc.setBlock(x + 1, y, z + 3, 35,current_block)
        cell2 = current_block
    if a ==3 and cell3==0:
        mc.setBlock(x + 1, y, z + 5, 35,current_block)
        cell3 = current_block
    if a ==4 and cell4==0:
        mc.setBlock(x + 3, y, z + 1, 35,current_block)
        cell4 = current_block
    if a == 5 and cell5==0:
        mc.setBlock(x + 3, y, z + 3, 35,current_block)
        cell5 = current_block
    if a == 6 and cell6==0:
        mc.setBlock(x + 3, y, z + 5, 35,current_block)
        cell6 = current_block
    if a == 7 and cell7==0:
        mc.setBlock(x + 5, y, z + 1, 35,current_block)
        cell7 = current_block
    if a == 8 and cell8==0:
        mc.setBlock(x + 5, y, z + 3, 35,current_block)
        cell8 = current_block
    if a == 9 and cell9==0:
        mc.setBlock(x + 5, y, z + 5, 35,current_block)
        cell9 = current_block
    if current_block==blue_block:
        current_block=red_block
    else:
        current_block=blue_block
    if cell1==cell2==cell3!=0:
        print ('WIN')
        winer=cell2
        break
    if cell4==cell5==cell6!=0:
        print ('WIN')
        winer = cell5
        break
    if cell7 == cell8 == cell9 != 0:
        print('WIN')
        winer = cell7
        break
    if cell1 == cell4 == cell7 != 0:
        print('WIN')
        winer = cell4
        break
    if cell3 == cell5 == cell7 != 0:
        print('WIN')
        winer = cell5
        break
    if cell1 == cell5 == cell9 != 0:
        print('WIN')
        winer = cell5
        break
    if cell2 == cell5 == cell8 != 0:
        print('WIN')
        winer = cell5
        break
    if cell3 == cell6 == cell9 != 0:
        print('WIN')
        break
    if cell1!=0 and cell2!=0 and cell3!=0 and cell4!=0 and cell5!=0 and cell6!=0 and cell7!=0 and cell8!=0 and cell9!=0:
        print ('нічія🟨')
        break
if winer!=0:
    if winer==blue_block:
        print('перемога синього🔵')
        mc.postToChat('WIN')
        mc.postToChat('перемога синього🔵')
    else:
        print ('перемога червоного🔴')
        mc.postToChat('WIN')
        mc.postToChat('перемога червоного🔴')
