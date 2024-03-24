bl_info = {
    "name" : "Chip Generator",
    "author" : "Izzy",
    "version" : (1, 0),
    "blender" : (4, 0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add mesh"
        
}
    
import bpy #allow you to interact with blender
from typing import List

class ChipCreator(bpy.types.Operator):
    #function for creating a singular chip object
    bl_idname = "OT_ChipCreator"
    bl_label = "Chip Create"    
    
    def execute(self, context):
        # Implement your second function here
        size: float = 1.0
        location: List[float] = [0.0, 0.0, 0.0]
        rotation: List[float] = [0.0, 0.0, 0.0]
        scale: List[float] = [2.0, 2.0, 2.0]
    
        bpy.ops.mesh.primitive_cube_add(
            size = size,
            calc_uvs = True,
            enter_editmode = False,
            align = 'WORLD',
            location = location,
            rotation = rotation,
            scale = scale
        )
        
        self.report({'INFO'}, f"This is {self.bl_idname}")
        return {'FINISHED'}
    

class GeneratePanel(bpy.types.Panel):
    bl_label = "Generate pile"
    bl_idname = "PT_GeneratePanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Generator'
    
    def draw(self,context):
        layout = self.layout
        
        row = layout.row() #adds space
        row.label(text = "Generate Pile", icon = 'CUBE')
        row = layout.row() #adds space
        row.operator("mesh.primitive_cube_add(size = size,calc_uvs = True,enter_editmode = False,align = 'WORLD',location = location,rotation = rotation,scale = scale)")
        #row.operator(ChipCreator.bl_idname, text = "Generate")

        
def register():
    bpy.utils.register_class(GeneratePanel)
    #bpy.utils.register_class(ChipCreator)
    
    
def unregister():
    bpy.utils.unregister_class(GeneratePanel)
    #bpy.utils.unregister_class(ChipCreator)
    
    
if __name__ == "__main__":
    register()
    
    
