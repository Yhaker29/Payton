from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
Pos = mc.player.getPos()
x=Pos.x
y=Pos.y
z=Pos.z
a=input ('🫵Ти хочеш побудувати будинок❔')
if a == 'Так':
    b=input ('Який доміщще ви шочите бобудувати❔')
    if b=='Великий':
        mc.setBlocks(x, y, z, x + 4, y + 4, z + 4, 41)
        mc.setBlocks(x+1,y+1,z+1,x+3,y+3,z+3,0)
        print ('Великий будинок заспавнився✅')
    else:
        mc.setBlock(x,y,z,82)
        print ('Маленький будинок заспавнився✅')
else :
    b=input ('Може басеін побудувати❔')
    if b==('Так'):
        pass
    else:
        c=input ('Чи хочите ви телепортнутись❔')
        if c=='Так':
            mc.player.setPos(0,0,0)
        else:
            print ('Ви нічого не надумали зробити то ви вільні!!!')
