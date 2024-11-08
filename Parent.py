import maya.cmds as cmds

def group_selected_objects():
    selection = cmds.ls(selection=True)
    
    for obj in selection:
        position = cmds.xform(obj, query=True, worldSpace=True, translation=True)
        rotation = cmds.xform(obj, query=True, worldSpace=True, rotation=True)
       
        group_name = f"{obj}_Grp"
        group = cmds.group(empty=True, name=group_name)
        
        cmds.xform(group, worldSpace=True, translation=position)
        cmds.xform(group, worldSpace=True, rotation=rotation)
        
        cmds.parent(obj, group)
       
group_selected_objects()
