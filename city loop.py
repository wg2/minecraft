import mcpi.minecraft as minecraft
import mcpi.block as block
import random
mc = minecraft.Minecraft.create()

#get position of player
pos = mc.player.getTilePos()            

#put first building 2 blocks x from player position
x = pos.x+2
y = pos.y
z = pos.z

height = random.randint(y+5,y+20)        #random building height

#loop to create row of randomly spaced buildings with random height
for loop in range(5):
    mc.setBlocks(x, y, z, x+2, height, z+2, block.GLASS.id)
    x = x + random.randint(x+5,x+20)    #randomly space next buildings
    height = random.randint(y+5,y+20)        #change next building height

