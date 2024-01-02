from bpy import utils
from bpy.types import Context, Menu, Panel, VIEW3D_MT_add
from topmod.addon.creation import operators


class TopmodCreationPanel(Panel):
    bl_label = "Creation"
    bl_category = "Topmod"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context: Context):
        self.layout.operator(
            operators.CreateManifoldFromMeshOperator.bl_idname,
        )
        self.layout.operator(
            operators.CreateManifoldPrimitiveOperator.bl_idname,
        )


class TopmodAddSubmenu(Menu):
    bl_idname = "TOPMOD_MT_add_menu"
    bl_label = "Topmod Manifold"

    def draw(self, context: Context | None):
        self.layout.separator()
        self.layout.operator(
            operator=operators.CreateManifoldPrimitiveOperator.bl_idname,
            text="Primitive",
        )


def add_menu_draw(menu: Menu, context: Context):
    menu.layout.separator()
    menu.layout.menu(TopmodAddSubmenu.bl_idname, icon="OUTLINER_OB_MESH")


CLASSES = (
    TopmodCreationPanel,
    TopmodAddSubmenu,
)


def register():
    for cls in CLASSES:
        utils.register_class(cls)
    VIEW3D_MT_add.append(add_menu_draw)


def unregister():
    for cls in CLASSES:
        utils.unregister_class(cls)
    VIEW3D_MT_add.remove(add_menu_draw)
