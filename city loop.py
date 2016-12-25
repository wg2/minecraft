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

#loop to create row of randomly spaced buildings
for loop in range(5):
    mc.setBlocks(x, y, z, x+2, y+10, z+2, block.GLASS.id)
    x = x + random.randint(x+5,x+20)    #randomly space next buildings
    z = random.randint(z+5,z+20)        #random building height

