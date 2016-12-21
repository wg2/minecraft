import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z
mc.setBlocks(x, y, z, x+2, y+10, z+2, block.GLASS.id)
mc.setBlocks(x+4, y, z, x+6, y+10, z+2, block.GLASS.id)
mc.setBlocks(x+8, y, z, x+10, y+10, z+2, block.GLASS.id)
mc.setBlocks(x+12, y, z, x+14, y+10, z+2, block.GLASS.id)
mc.setBlocks(x, y, z+4, x+2, y+10, z+6, block.GLASS.id)
mc.setBlocks(x+4, y, z+8, x+6, y+10, z+10, block.GLASS.id)
mc.setBlocks(x+8, y, z+12, x+10, y+10, z+14, block.GLASS.id)
mc.setBlocks(x+4, y, z+4, x+6, y+10, z+6, block.GLASS.id)
mc.setBlocks(x+8, y, z+4, x+10, y+10, z+6, block.GLASS.id)
mc.setBlocks(x+12, y, z+4, x+14, y+10, z+6, block.GLASS.id)
mc.setBlocks(x, y, z+8, x+2, y+10, z+10, block.GLASS.id)
mc.setBlocks(x+8, y, z+8, x+10, y+10, z+10, block.GLASS.id)
mc.setBlocks(x+12, y, z+8, x+14, y+10, z+10, block.GLASS.id)
mc.setBlocks(x, y, z+12, x+2, y+10, z+14, block.GLASS.id)
mc.setBlocks(x+4, y, z+12, x+6, y+10, z+14, block.GLASS.id)
mc.setBlocks(x+12, y, z+12, x+14, y+10, z+14, block.GLASS.id)