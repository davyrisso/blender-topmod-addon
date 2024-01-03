from bpy import utils
from bpy.types import Context, Menu, Panel, VIEW3D_MT_add
from topmod.addon.creation import operators


class TOPMOD_PT_create_panel(Panel):
    bl_idname = "TOPMOD_PT_create_panel"
    bl_label = "Manifold Creation"
    bl_category = "Topmod"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context: Context):
        self.layout.operator(
            operators.TOPMOD_OT_create_manifold_from_mesh.bl_idname,
        )
        self.layout.operator(
            operators.TOPMOD_OT_create_manifold_primitive.bl_idname,
        )


class TOPMOD_MT_add_menu(Menu):
    bl_idname = "TOPMOD_MT_add_menu"
    bl_label = "Topmod Manifold"

    def draw(self, context: Context | None):
        self.layout.separator()
        self.layout.operator(
            operator=operators.TOPMOD_OT_create_manifold_primitive.bl_idname,
            text="Primitive",
        )

    @staticmethod
    def add_menu_draw(menu: Menu, context: Context):
        menu.layout.separator()
        menu.layout.menu(TOPMOD_MT_add_menu.bl_idname, icon="OUTLINER_OB_MESH")


CLASSES = (
    TOPMOD_PT_create_panel,
    TOPMOD_MT_add_menu,
)


def register():
    for cls in CLASSES:
        utils.register_class(cls)
    VIEW3D_MT_add.append(TOPMOD_MT_add_menu.add_menu_draw)


def unregister():
    for cls in CLASSES:
        utils.unregister_class(cls)
    VIEW3D_MT_add.remove(TOPMOD_MT_add_menu.add_menu_draw)
