from nicegui import ui

def show_footer():
    with ui.footer().classes('bg-black text-white p-4 mt-10'):
        ui.label('© 2025 SkillBridge. All rights reserved.')