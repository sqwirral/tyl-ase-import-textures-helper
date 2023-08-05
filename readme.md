# ASE import textures helper

Fixes most of the textures after importing an ASE model (Quake 3 engine stuff, from GtkRadiant/Q3Map2) into Blender using mrwonko's ASE Import script:
https://github.com/mrwonko/Blender-Jedi-Academy-Tools/

Only JPG/TGA. Some textures won't work for various reasons, such as if they're pointing at code in .shader files instead. But wcyd.

Edit the `tex_dir` path to tell it where to find stuff. Open the System Console to get a brief report.

Written for blender 3.6.