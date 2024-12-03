import maya.cmds as cmds

for obj in cmds.ls(selection=True):
    for shape in cmds.listRelatives(obj, shapes=True, fullPath=True) or []:
        cmds.setAttr(f"{shape}.overrideEnabled", 1)
        cmds.setAttr(f"{shape}.overrideColor", 13)
