# tyl - ase import textures helper
# 4th august 2023

import bpy
from pathlib import Path

# edit this to point to your textures
tex_dir = "C:/Program Files (x86)/Wolfenstein - Enemy Territory/etmain/"

# just used to count and print the totals to the system console
num_mats_found = 0
num_mats_edited = 0
num_texs_loaded = 0
num_texs_found = 0
    
# iterate over the materials
for m in bpy.data.materials:
    
    # skip if it's the grease pencil material ('Dots Stroke')
    if not m.is_grease_pencil:
            
        # enable Use Nodes for this material
        m.use_nodes = True
         
        # skip if there's already something connected to the Base Color
        if not m.node_tree.nodes["Principled BSDF"].inputs['Base Color'].is_linked:
            
            # add Image Texture node
            m.node_tree.nodes.new('ShaderNodeTexImage')
            
            # link the nodes
            m.node_tree.links.new(
              m.node_tree.nodes["Image Texture"].outputs['Color'],
              m.node_tree.nodes["Principled BSDF"].inputs['Base Color']
            )
            m.node_tree.links.new(
              m.node_tree.nodes["Image Texture"].outputs['Alpha'],
              m.node_tree.nodes["Principled BSDF"].inputs['Alpha']
            )
        
            # count materials edited
            num_mats_edited += 1
            
        # expand the input ui in material properties
        m.node_tree.nodes["Principled BSDF"].inputs[0].show_expanded = True
        
        # skip if there's already an image loaded in this Image Texture node
        if not hasattr(m.node_tree.nodes["Image Texture"].image, 'id_data'):
        
            # check if JPG file exists
            file = Path(tex_dir + m.name + ".jpg")
            if file.exists():
                
                # load texture file
                m.node_tree.nodes["Image Texture"].image = bpy.data.images.load(tex_dir + m.name + ".jpg")
                
                # count textures loaded
                num_texs_loaded += 1
        
            # check if TGA file exists
            file = Path(tex_dir + m.name + ".tga")
            if file.exists():
                
                # load texture file
                m.node_tree.nodes["Image Texture"].image = bpy.data.images.load(tex_dir + m.name + ".tga")
                
                # count textures loaded
                num_texs_loaded += 1
                
        else:
            
            # count textures found
            num_texs_found += 1
                
        # count materials found
        num_mats_found += 1

print("---")      
print("Script complete!")
print("  Materials edited : " + str(num_mats_edited))
print("  Textures loaded  : " + str(num_texs_loaded))
print("  Total materials  : " + str(num_mats_found) + " (" 
      + str(num_mats_found - num_texs_found - num_texs_loaded) + " textures missing)")