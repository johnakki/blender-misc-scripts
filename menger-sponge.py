import bpy
level = 3
hole_ids = [4, 10, 12, 13, 14, 16, 22]

bpy.ops.mesh.primitive_cube_add()

for i in range(0,level):
    cube = bpy.context.active_object

    dim_x = cube.dimensions[0]
    dim_y = cube.dimensions[1]
    dim_z = cube.dimensions[2]

    id = 0
    cubes = []
    for trn_x in range(0,3):
        for trn_y in range(0,3):
            for trn_z in range(0,3):
                if id not in hole_ids:
                    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(dim_x*trn_x,dim_y*trn_y,dim_z*trn_z)})
                    cubes.append(bpy.context.active_object)
                    bpy.context.active_object.select_set('DESELECT')
                    cube.select_set('SELECT')
                id+=1
    for cube in cubes:
        cube.select_set('SELECT')
    bpy.ops.object.join()
    
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.remove_doubles()
bpy.ops.object.mode_set(mode='OBJECT')
