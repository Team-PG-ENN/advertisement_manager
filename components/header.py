from nicegui import ui

def show_header():
    ui.query('.nicegui.contents').classes('m-0 p-0 gap-0')
    with ui.header().classes('items-center justify-between'):
        with ui.row().classes('items-center'):
            ui.image(source="/assets/logo.png").classes('w-8 h-8')
            ui.label("Skildge").classes("no-underline text-black font-lobster")
        
   
        
    with ui.row():
            ui.link("Home").classes("no-underline")
            ui.link("Jobs").classes("no-underline")
            ui.link("Resources").classes("no-underline")
            ui.link("Partners").classes("no-underline")
    with ui.row():
            ui.button("Login").props("no-caps flat").classes("rounded text-lg")
            ui.button("Sign Up").props("no-caps").classes("rounded text-lg")
            ui.button("Post a Job").props("no-caps flat").classes("bg-orange-400 text-white text-lg")






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
