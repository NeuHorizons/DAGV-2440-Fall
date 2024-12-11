import maya.cmds as cmds

class SequentialRenamerUI:
    def __init__(self):
        self.window = "SequentialRenamerWindow"
        self.text_field = None

    def create(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)
        self.window = cmds.window(title="Sequential Renamer", widthHeight=(300, 100))
        cmds.columnLayout(adjustableColumn=True)
        cmds.text(label="Enter Naming Scheme:")
        self.text_field = cmds.textField()
        cmds.button(label="Rename", command=self.rename_objects)
        cmds.showWindow(self.window)

    def rename_objects(self, *args):
        naming_scheme = cmds.textField(self.text_field, query=True, text=True)
        selected_objects = cmds.ls(selection=True)
        prefix, suffix = naming_scheme.split("#" * naming_scheme.count("#"), 1)
        for i, obj in enumerate(selected_objects, start=1):
            cmds.rename(obj, f"{prefix}{i:0{naming_scheme.count('#')}d}{suffix}")

class AssignColorUI:
    def __init__(self):
        self.window = "AssignColorWindow"

    def create(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)
        self.window = cmds.window(title="Assign Color", widthHeight=(300, 150))
        cmds.columnLayout(adjustableColumn=True)
        cmds.text(label="Select a Color:")
        colors = {"Red": 13, "Blue": 6, "Green": 14, "Yellow": 17}
        for color_name, color_value in colors.items():
            cmds.button(label=color_name, backgroundColor=self.get_rgb(color_value),
                        command=lambda _, cv=color_value: self.assign_color(cv))
        cmds.showWindow(self.window)

    def assign_color(self, color_value):
        selected_objects = cmds.ls(selection=True)
        for obj in selected_objects:
            for shape in cmds.listRelatives(obj, shapes=True, fullPath=True) or []:
                cmds.setAttr(f"{shape}.overrideEnabled", 1)
                cmds.setAttr(f"{shape}.overrideColor", color_value)

    def get_rgb(self, color_index):
        return {
            13: (1.0, 0.0, 0.0),
            6: (0.0, 0.0, 1.0),
            14: (0.0, 1.0, 0.0),
            17: (1.0, 1.0, 0.0)
        }.get(color_index, (0.5, 0.5, 0.5))

renamer_ui = SequentialRenamerUI()
renamer_ui.create()

color_ui = AssignColorUI()
color_ui.create()
