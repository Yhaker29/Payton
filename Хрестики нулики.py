import random

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
Pos = mc.player.getTilePos()
x=-30
y=-15
z=-1
print(Pos)

winer=0
red_block=14
blue_block=11
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



while True:
    i,block1=mc.getBlockWithData(x+1,y,z+1)
    i,block2=mc.getBlockWithData(x+1,y,z+3)
    i,block3=mc.getBlockWithData(x+1,y,z+5)
    i,block4=mc.getBlockWithData(x+3,y,z+1)
    i,block5=mc.getBlockWithData(x+3,y,z+3)
    i,block6=mc.getBlockWithData(x+3,y,z+5)
    i,block7=mc.getBlockWithData(x+5,y,z+1)
    i,block8=mc.getBlockWithData(x+5,y,z+3)
    i,block9=mc.getBlockWithData(x+5,y,z+5)
    if block1!=216 and cell1==0:
        cell1=block1
    # else:
    #     mc.setBlock(x+1,y,z+1,cell1) #1
    if block2!=216 and cell2==0:
        cell2=block2
    # else:
    #     mc.setBlock(x + 1, y, z + 3, 216)  # 2
    if block3 !=216 and cell3==0:
        cell3=block3
    # else:
    #     mc.setBlock(x + 1, y, z + 5, 216)  # 3
    if block4!=216 and cell4==0:
        cell4=block4
    # else:
    #     mc.setBlock(x + 3, y, z + 1, 216)  # 4
    if block5!=216 and cell5==0:
        cell5=block5
    # else:
    #     mc.setBlock(x + 3, y, z + 3, 216)  # 5
    if block6!=216 and cell6==0:
        cell6=block6
    # else:
    #     mc.setBlock(x + 3, y, z + 5, 216)  # 6
    if block7!=216 and cell7==0:
        cell7=block7
    # else:
    #     mc.setBlock(x + 5, y, z + 1, 216)  # 7
    if block8!=216 and cell8==0:
        cell8=block8
    # else:
    #     mc.setBlock(x + 5, y, z + 3, 216)  # 8
    if block9!=216 and cell9==0:
        cell9=block9
    # else:
    #    mc.setBlock(x + 5, y, z + 5, 216)  # 9
    time.sleep(1)



    if cell1==cell2==cell3!=0:
        print ('WIN',cell1,cell2,cell3,cell4,cell5,cell6,cell7,cell8)
        winer=cell2
    if cell4==cell5==cell6!=0:
        print ('WIN')
        winer = cell5
    if cell7 == cell8 == cell9 != 0:
        print('WIN')
        winer = cell7
    if cell1 == cell4 == cell7 != 0:
        print('WIN')
        winer = cell4
    if cell3 == cell5 == cell7 != 0:
        print('WIN')
        winer = cell5
    if cell1 == cell5 == cell9 != 0:
        print('WIN')
        winer = cell5
    if cell2 == cell5 == cell8 != 0:
        print('WIN')
        winer = cell5
    if cell3 == cell6 == cell9 != 0:
        print('WIN')
        winer = cell6
    if cell1 != 0 and cell2 != 0 and cell3 != 0 and cell4 != 0 and cell5 != 0 and cell6 != 0 and cell7 != 0 and cell8 != 0 and cell9 != 0:
        print('нічія🟨')
        mc.postToChat('нічія🟨')
    if winer!=0:
        if winer==blue_block:
            print('перемога синього🔵')
            mc.postToChat('WIN')
            mc.postToChat('перемога синього🔵')
        if winer==red_block:
            print ('перемога червоного🔴')
            mc.postToChat('WIN')
            mc.postToChat('перемога червоного🔴')
    print ('cells',cell1,cell2,cell3,cell4,cell5,cell6,cell7,cell8,cell9)
    restard=mc.getBlock(-23,-15,2)
    if restard==46:
        print('RESTART🔃')
        mc.postToChat('RESTART🔃')
        mc.setBlock(-23,-15,2,0)
        mc.setBlocks(x, y, z, x + 6, y, z + 6, 41)
        mc.setBlock(x + 1, y, z + 1, 216)  # 1
        mc.setBlock(x + 1, y, z + 3, 216)  # 2
        mc.setBlock(x + 1, y, z + 5, 216)  # 3
        mc.setBlock(x + 3, y, z + 1, 216)  # 4
        mc.setBlock(x + 3, y, z + 3, 216)  # 5
        mc.setBlock(x + 3, y, z + 5, 216)  # 6
        mc.setBlock(x + 5, y, z + 1, 216)  # 7
        mc.setBlock(x + 5, y, z + 3, 216)  # 8
        mc.setBlock(x + 5, y, z + 5, 216)  # 9
        cell1 = 0
        cell2 = 0
        cell3 = 0
        cell4 = 0
        cell5 = 0
        cell6 = 0
        cell7 = 0
        cell8 = 0
        cell9 = 0
        winer=0
    elif restard!=0:
        print('FINISH✅')
        mc.setBlock(-23, -15, 2, 0)
        mc.setBlocks(x, y, z, x + 6, y, z + 6, 41)
        mc.setBlock(x + 1, y, z + 1, 216)  # 1
        mc.setBlock(x + 1, y, z + 3, 216)  # 2
        mc.setBlock(x + 1, y, z + 5, 216)  # 3
        mc.setBlock(x + 3, y, z + 1, 216)  # 4
        mc.setBlock(x + 3, y, z + 3, 216)  # 5
        mc.setBlock(x + 3, y, z + 5, 216)  # 6
        mc.setBlock(x + 5, y, z + 1, 216)  # 7
        mc.setBlock(x + 5, y, z + 3, 216)  # 8
        mc.setBlock(x + 5, y, z + 5, 216)  # 9
        cell1 = 0
        cell2 = 0
        cell3 = 0
        cell4 = 0
        cell5 = 0
        cell6 = 0
        cell7 = 0
        cell8 = 0
        cell9 = 0
        mc.postToChat('FINISH✅')
        break