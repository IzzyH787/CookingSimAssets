bl_info = {
    "name" : "Object Adder",
    "author" : "Izzy",
    "version" : (1, 0),
    "blender" : (4, 0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add mesh",
}

import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom'
    
    def draw(self,context):
        layout = self.layout
        
        row = layout.row() #adds space
        row.label(text = "Sample text", icon = 'CUBE')
        row = layout.row() #adds space
        row.operator("mesh.primitive_cube_add")
        row = layout.row() #adds space
        row.operator("mesh.primitive_uv_sphere_add")
 
 
 
 
 
        
class PanelA(bpy.types.Panel):
    bl_label = "Scaling"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom'
    bl_parent_id = 'PT_TestPanel'
    bl_options = {'DEFAULT_CLOSED'} #panels closed by default
    
    def draw(self,context):
        
        #declaring variables for easy access to properties
        layout = self.layout
        obj = context.object
        
        col = layout.column()
        
        row = layout.row() #adds space
        row.label(text = "Select a scaling option:", icon = 'FONT_DATA')
        row = layout.row() #adds space
        row.operator("transform.resize")
        row = layout.row() #adds space
        layout.scale_y = 1.2 #sets height scale of rows in panel
        col.prop(obj, "scale") #separate scales into 1 column
   
   
   
   
   
        
class PanelB(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_PanelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom'
    bl_parent_id = 'PT_TestPanel'
    bl_options = {'DEFAULT_CLOSED'} #panels closed by default
    
    def draw(self,context):
        layout = self.layout

        row = layout.row() #adds space
        
        row.label(text = "Select a specials option:", icon = 'FONT_DATA')
        
        row = layout.row() #adds space
           
        row.operator("object.shade_smooth", icon = "MOD_SMOOTH", text = "Set Smooth Shading")
        
        row = layout.row() #adds space
        
        row.operator("object.subdivision_set")
        row = layout.row() #adds space
        row.operator("object.modifier_add")
       
               
  
        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
    

    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.register_class(PanelB)
    
    
if __name__ == "__main__":
    register()