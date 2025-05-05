import time

import dearpygui.dearpygui as dpg
import myextension
from sample_utils import enable_windows_dark_titlebar

WINDOW_SECONDS = 5.0  # show last 5 seconds on screen
SAMPLE_FREQ = 100.0  # 100 updates per second

dpg.create_context()
with dpg.font_registry():
    app_font = dpg.add_font("sample/fonts/Archivo-Regular.ttf", 14)
dpg.bind_font(app_font)
dpg.create_viewport(title="Sample", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
enable_windows_dark_titlebar("Sample")

with dpg.window(label="Oscilloscope", pos=(50, 50), no_collapse=True, width=650, height=400), dpg.plot(label="sim_value(t)", height=350, width=600):
    # give the axes tags so we can manipulate them
    x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="Time (s)", tag="x_axis")
    y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="Value", tag="y_axis")
    dpg.set_axis_limits("y_axis", -1.5, 1.5)
    series = dpg.add_line_series([], [], parent=y_axis, tag="series")

# 2) Buffers for the last WINDOW_SECONDS of data
xs, ys = [], []
t0 = time.time()


def update_frame() -> None:
    # compute current time relative to start
    t = time.time() - t0
    # sample your C++ function
    y = myextension.sim_value(t)

    # append new data
    xs.append(t)
    ys.append(y)

    # remove old points past WINDOW_SECONDS ago
    cutoff = t - WINDOW_SECONDS
    while xs and xs[0] < cutoff:
        xs.pop(0)
        ys.pop(0)

    # 3) update the series and the x-axis limits
    dpg.set_value(series, (xs, ys))
    dpg.set_axis_limits("x_axis", cutoff if cutoff > 0 else 0, t)

    # schedule next update at the next frame
    next_frame = dpg.get_frame_count() + 1
    dpg.set_frame_callback(next_frame, update_frame)


# kick off the first update but delay by 2 frames because the dark mode goes on frame 1
dpg.set_frame_callback(dpg.get_frame_count() + 2, update_frame)

dpg.start_dearpygui()
dpg.destroy_context()
