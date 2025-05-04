import ctypes
import sys
from ctypes import wintypes

import dearpygui.dearpygui as dpg


def enable_windows_dark_titlebar(window_title: str) -> None:
    """
    On Windows 10/11, schedule the DWM immersive-dark-mode flag
    for the DearPyGui viewport whose title matches `window_title`.
    """
    if sys.platform != "win32":
        return

    def _apply() -> None:
        # look up the HWND by window title
        hwnd = ctypes.windll.user32.FindWindowW(None, window_title)
        if not hwnd:
            return  # not ready yet; next frame will retry

        # choose the right attribute index
        build = sys.getwindowsversion().build
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20 if build >= 19041 else 19

        # turn on dark title bar
        val = ctypes.c_int(1)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(wintypes.HWND(hwnd), ctypes.c_uint(DWMWA_USE_IMMERSIVE_DARK_MODE), ctypes.byref(val), ctypes.sizeof(val))

    # run on the very next frame so the OS window has been created
    next_frame = dpg.get_frame_count() + 1
    dpg.set_frame_callback(next_frame, _apply)
