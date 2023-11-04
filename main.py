import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(tag="Color picker window"):
    dpg.add_color_picker()

dpg.create_viewport(title='Color picker by Bt08s', width=600, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Color picker window", True)
dpg.start_dearpygui()
dpg.destroy_context()
