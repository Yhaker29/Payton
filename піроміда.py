from mcpi.minecraft import Minecraft
import random
import time

# mc = Minecraft.create()
# Pos = mc.player.getTilePos()
# x=Pos.x
# y=Pos.y
# z=Pos.z
#
# b=0
# a=0
# for aa in range(8):
#     for i in range(8):
#         mc.setBlock(x+a,y,z+b,1)
#         a+=1
#     b+=1
#     a=0
# mc.setBlocks(x,y,z,x+7,y,z+7,41)
# mc.setBlocks(x+1,y+1,z+1,x+6,y+1,z+6,42)
# mc.setBlocks(x+2,y+2,z+2,x+5,y+2,z+5,45)
# mc.setBlocks(x+3,y+3,z+3,x+4,y+3,z+4,46)

# Hacer=250
# a=Hacer*2-1
# b=0
# c=0
# for i in range (Hacer):
#     mc.setBlocks(x+c,y+b,z+c,x+a,y+b,z+a,41)
#     a-=1
#     b+=1
#     c+=1


# a=0
# for i in range(100):
#     for k in range(5):
#         b=random.randint(0,15)
#         mc.setBlock(x+a,y+i,z,35,b)
#         a+=1
#     a=0
# a=0
# for i in range(21):
#     a+=i
#     print(a)
# a=0
# while True:
#     print(a)
#     a+=1
#     if a==10000:
#         break
очки=0
a=random.randint(1,10)
d=5
while True:
    print(d*"❤️",)
    b=int(input('Ведіть ваше число🔍'))
    if b==a:
        print('Вітаю! Ви вгадали число✅')
        if(d==5):
            очки+=300
        if (d == 4):
            очки += 250
        if (d == 3):
            очки += 150
        if (d == 2):
            очки += 80
        if (d == 1):
            очки += 30
        print('У вас', очки, 'очків😮!')
        break
    else:
        print ('Пробачте! Ви не вгадали число❌')
        d=d-1
        if d==0:
            print ('Компюнтер загадав число ',a,)
            print('У вас',очки,'очків😮!')
            break
