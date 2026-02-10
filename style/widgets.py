import flet as ft
from . import colors as c

def styled_textfield(label="URL", hint="Paste the URL", width=600):
    return ft.TextField(
        label=label,
        width=width,
        color=c.TEXTFIELD_TEXT,
        bgcolor=c.TEXTFIELD_BG,
        border_color=c.TEXTFIELD_BORDER,
        border_radius=6,
        focused_border_color=c.TEXTFIELD_FOCUSED_BORDER,
        label_style=ft.TextStyle(color=c.TEXTFIELD_LABEL),
        hint_text=hint,
        hint_style=ft.TextStyle(color=c.TEXTFIELD_HINT)
    )

def styled_button(text, icon=None, bgcolor=c.BTN_VIDEO, on_click=None):
    return ft.Button(
        text,
        icon=icon,
        icon_color=c.BTN_TEXT,
        bgcolor=bgcolor,
        color=c.BTN_TEXT,
        on_click=on_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            elevation=5,
            overlay_color=c.BTN_OVERLAY
        )
    )