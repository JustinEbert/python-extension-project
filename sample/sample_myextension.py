import dearpygui.dearpygui as dpg
import myextension

# Initialize the extension and acquire some data from it
myextension.initialize()
results = [myextension.step(1.0).current_mass for _ in range(5)]

# Initialize DearPyGui and create a viewport
dpg.create_context()
with dpg.font_registry():
    app_font = dpg.add_font("sample/fonts/Archivo-Regular.ttf", 14)
dpg.bind_font(app_font)
dpg.create_viewport(title="My Extension Sample", width=800, height=600)

# Plot some data from the extension, showing that the C++ bindings work
with dpg.window(label="Extension Data Plot"):
    with dpg.plot(label="Extension Data", height=400, width=500):
        dpg.add_plot_axis(dpg.mvXAxis, label="Index")
        dpg.add_plot_axis(dpg.mvYAxis, label="Value", tag="y_axis")
        dpg.add_line_series(list(range(len(results))), list(results), label="Data", parent="y_axis")

# Clean up
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
