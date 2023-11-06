import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(tag="Color picker window"):
    dpg.add_color_picker()

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 3)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 3)
        dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 3)
        dpg.add_theme_style(dpg.mvStyleVar_TabRounding, 3)
        dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 3)
        dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 3)
        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 3)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 4, 4)
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 5, 5)

dpg.bind_theme(global_theme)
dpg.create_viewport(title='Color picker by Bt08s', width=600, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Color picker window", True)
dpg.start_dearpygui()
dpg.destroy_context()
