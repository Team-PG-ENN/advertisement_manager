from nicegui import ui

def show_header():
    ui.query('.nicegui.contents').classes('m-0 p-0 gap-0')
    with ui.row().classes("w-full flex justify-between items-center text-lg flex-wrap py-3 px-10 sticky"):
        with ui.row():
            #ui.image("")
            ui.link("SkillBridge", "/").classes("no-underline text-black font-lobster")
        with ui.row():
            ui.link("Home").classes("no-underline")
            ui.link("Jobs").classes("no-underline")
            ui.link("Resources").classes("no-underline")
            ui.link("Partners").classes("no-underline")
        with ui.row():
            ui.button("Login").props("no-caps flat").classes("rounded text-lg")
            ui.button("Sign Up").props("no-caps").classes("rounded text-lg")
            ui.button("Post a Job").props("no-caps flat").classes("bg-orange-400 text-white text-lg")