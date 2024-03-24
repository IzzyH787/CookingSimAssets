import bpy
import random

YellowMaterial = 'Material.Red'

def GenerateFry():
    size: float = 1.0
    spacing = 2
    
    XScale = random.uniform(0.2,0.4)
    ZScale = XScale
    YScale = random.uniform(3,10)
    
    rotateScale = random.uniform(-10,10)
    
    XPosition = random.uniform(-5,5)
    YPosition = random.uniform(-5,5)
    ZPosition = random.uniform(0,1)
    
    location: List[float] = [XPosition, YPosition, ZPosition]
    rotation: List[float] = [rotateScale, rotateScale, random.uniform(-180,180)]
    scale: List[float] = [XScale, YScale, ZScale]
    
    bpy.ops.mesh.primitive_cube_add(
        size = size,
        calc_uvs = True,
        enter_editmode = False,
        align = 'WORLD',
        location = location,
        rotation = rotation,
        scale = scale,
    )
    
    #item = bpy.context.object
    #item.data.materials.append(bpy.data.materials['Material.Red'])
    
    
#    for i in bpy.data.objects:
#        if i.name.startswith("Cube"):
#            # Select object:
#            bpy.ops.object.select_name(name=i.name)
#            # Add modifier:
#            bpy.ops.object.modifier_add(type='COLLISION')
class generator:
    bl_idname =
     def GeneratePile(pileSize):
         if(pileSize == 1):
             for i in range(15):
                 generateFry()
         elif(pileSize == 2):
             for i in range(30):
                generateFry()
         elif(pileSize == 3):
             for i in range(45):
                generateFry()
         elif(pileSize == 4):
             for i in range(60):
                generateFry()
         elif(pileSize >= 5):
             for i in range(75):
                generateFry()
            
            

class GeneratorPanel(bpy.types.Panel):
    bl_label = "Generate Panel"
    bl_idname = "PT_GeneratorPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Generate'
    
    def draw(self,context):
        layout = self.layout
        
        row = layout.row() #adds space
        row.label(text = "Generate a pile:", icon = 'CUBE')
        row = layout.row() #adds space
        row.operator('execute(GeneratePile())')
        row = layout.row() #adds space
        #row.operator("mesh.primitive_uv_sphere_add")
        
def register():
    bpy.utils.register_class(GeneratorPanel)
      
def unregister():
    bpy.utils.unregister_class(GeneratorPanel)
    
if __name__ == "__main__":
    register()