from nicegui import ui

def show_header():
    ui.query('.nicegui.contents').classes('m-0 p-0 gap-0')
    with ui.header().classes('flex items-center justify-between bg-white'):
        with ui.row().classes('items-center'):
            ui.image(source="/assets/loggo.png").classes('w-14 h-18')
            # ui.label("Skillbridge").classes("no-underline text-black font-lobster")      
        with ui.row():
                ui.link("Home").classes("no-underline font-bold text-lg text-primary")
                ui.link("Jobs").classes("no-underline font-bold text-lg text-primary")
                ui.link("Resources").classes("no-underline font-bold text-lg text-primary")
                ui.link("Partners").classes("no-underline font-bold text-lg text-primary")
        with ui.row():
                ui.button("Login",on_click=lambda:ui.navigate.to("/vendor_signin")).props("no-caps flat").classes("rounded text-1 bg-white text-black font-bold rounded-full px-3 py-1 transition-transform transform hover:scale-105'") 
                ui.button("Sign Up", on_click=lambda:ui.navigate.to("/vendor_signup")).props("no-caps").classes("rounded text-1 text-white font-bold rounded-full px-3 py-1 transition-transform transform hover:scale-105'")
                ui.button("Post a Job").props("no-caps flat").classes("bg-orange-400 text-white text-1 bg-orange-400 text-white font-bold rounded-full px-3 py-1 transition-transform transform hover:scale-105'")






#             from nicegui import ui
# from pages.vendor_page import vendor_dashboard_page


# def show_header():
#     """Creates the persistent header component for all pages."""
#     with ui.header().classes(
#         'bg-white shadow-lg text-white items-center justify-between p-4'
#     ):
#         # LEFT: Logo
#         ui.label('Skillbridge').classes('text-2xl font-bold tracking-wide')

#         # CENTER: Explore buttons
#         with ui.row().classes('absolute left-1/2 transform -translate-x-1/2'):
#             with ui.button('Explore', icon='expand_more').classes('bg-white text-orange-500 font-semibold'):
#                 with ui.menu():
#                     ui.menu_item('Browse Jobs', lambda: ui.notify('Browse Jobs'))
#                     ui.menu_item('Companies', lambda: ui.notify('Companies'))
#                     ui.menu_item('Training Programs', lambda: ui.notify('Training'))
#                     ui.menu_item('Resources', lambda: ui.notify('Resources'))
#             with ui.button('Job Seekers', icon='expand_more').classes('text-orange-500 font-semibold'):
#                 with ui.menu():
#                     ui.menu_item('Browse Jobs', lambda: ui.notify('Browse Jobs'))
#                     ui.menu_item('Companies', lambda: ui.notify('Companies'))
#                     ui.menu_item('Training Programs', lambda: ui.notify('Training'))
#                     ui.menu_item('Resources', lambda: ui.notify('Resources'))
#             with ui.button('Employers', icon='expand_more').classes('text-orange-500 font-semibold'):
#                 with ui.menu():
#                     ui.menu_item('Browse Jobs', lambda: ui.notify('Browse Jobs'))
#                     ui.menu_item('Companies', lambda: ui.notify('Companies'))
#                     ui.menu_item('Training Programs', lambda: ui.notify('Training'))
#                     ui.menu_item('Resources', lambda: ui.notify('Resources'))

#         # RIGHT: Auth buttons
#         with ui.row().classes('items-center gap-3 ml-auto'):
#             ui.button('Login', on_click=show_login_modal).classes(
#                 'bg-blue text-orange-600 font-bold px-4 py-2 transition-transform transform hover:scale-105'
                
#             )
#             ui.button('Sign Up', on_click="").classes(
#                 'bg-blue text-orange-600 font-bold rounded-full px-4 py-2 transition-transform transform hover:scale-105'
#             )
# def show_login_modal():
#     """Show login modal with user type selection"""
#     with ui.dialog().props('persistent') as dialog, ui.card().classes('p-6'):
#         ui.label('Choose Login Type').classes('text-h6 mb-4 text-center')

#         with ui.column().classes('gap-4 items-center'):
#             # Login as Job Seeker → go to homepage (/)
#             ui.button(
#                 'Login as Job Seeker',
#                 on_click=lambda: (dialog.close(), ui.navigate.to('/'))
#             ).classes('primary-button w-full')

#             # Login as Company/Vendor → go to /vendor
#             ui.button(
#                 'Login as Company/Vendor',
#                 on_click=lambda: (dialog.close(), ui.navigate.to('/vendor'))
#             ).classes('nav-button w-full')

#             # Cancel → just close the dialog
#             ui.button(
#                 'Cancel',
#                 on_click=dialog.close
#             ).classes('nav-button w-full')

#     dialog.open()


# def login_as_user(dialog):
#     """Navigate to user dashboard"""
#     dialog.close()
#     ui.navigate.to('/user')

# def login_as_vendor(dialog):
#     """Navigate to vendor dashboard"""
#     dialog.close()
#     ui.navigate.to('/vendor')
