import maya.cmds as cmds

def rename_selection_in_maya(naming_scheme):
    selected_objects = cmds.ls(selection=True)
    num_hashes = naming_scheme.count("#")
    prefix, suffix = naming_scheme.split("#" * num_hashes, 1)
    for i, obj in enumerate(selected_objects, start=1):
        number = f"{i:0{num_hashes}d}"
        new_name = f"{prefix}{number}{suffix}"
        cmds.rename(obj, new_name)

rename_selection_in_maya("Leg_##_Jnt")
