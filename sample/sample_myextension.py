import math
import time

import dearpygui.dearpygui as dpg
import myextension
from sample_utils import enable_windows_dark_titlebar

# Initialize the extension and acquire some data from it
myextension.initialize()
results = [myextension.step(1.0).current_mass for _ in range(5)]

# Initialize DearPyGui load a font, and create a viewport
dpg.create_context()
with dpg.font_registry():
    app_font = dpg.add_font("sample/fonts/Archivo-Regular.ttf", 14)
dpg.bind_font(app_font)
dpg.create_viewport(title="Sample", width=800, height=600)

# Setup and make the window dark (has to be after the show_viewport)
dpg.setup_dearpygui()
dpg.show_viewport()
enable_windows_dark_titlebar("Sample")

# Plot some data from the extension, showing that the C++ bindings work
with dpg.window(label="Extension Data Plot"), dpg.plot(label="Extension Data", height=400, width=500):
    dpg.add_plot_axis(dpg.mvXAxis, label="Index")
    dpg.add_plot_axis(dpg.mvYAxis, label="Value", tag="y_axis")
    dpg.add_line_series(list(range(len(results))), list(results), label="Data", parent="y_axis")

# Go!
dpg.start_dearpygui()

# Clean up
dpg.destroy_context()
