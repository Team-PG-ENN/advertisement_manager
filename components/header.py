from nicegui import ui


def show_header():
    """Creates the persistent header component for all pages."""
    with ui.header().classes(
        'bg-orange shadow-lg text-white items-center justify-between p-4'
    ):
        # LEFT: Logo
        ui.label('Skillbridge').classes('text-2xl font-bold tracking-wide')

        # CENTER: Explore buttons
        with ui.row().classes('absolute left-1/2 transform -translate-x-1/2'):
            with ui.button('Explore', icon='expand_more').classes('bg-orange text-orange-500 font-semibold'):
                with ui.menu():
                    ui.menu_item('Browse Jobs', lambda: ui.notify('Browse Jobs'))
                    ui.menu_item('Companies', lambda: ui.notify('Companies'))
                    ui.menu_item('Training Programs', lambda: ui.notify('Training'))
                    ui.menu_item('Resources', lambda: ui.notify('Resources'))

        # RIGHT: Auth buttons
        with ui.row().classes('items-center gap-3 ml-auto'):
            ui.button('Login', on_click=show_login_modal).classes(
                'bg-black text-orange-600 font-semibold rounded-full px-4 py-2 transition-transform transform hover:scale-105'
                
            )
            ui.button('Sign Up', on_click="").classes(
                'bg-black text-orange-600 font-bold rounded-full px-4 py-2 transition-transform transform hover:scale-105'
            )
def show_login_modal():
    """Show login modal with user type selection"""
    with ui.dialog().props('persistent') as dialog, ui.card().classes('p-6'):
        ui.label('Choose Login Type').classes('text-h5 mb-4 text-center')
        
        with ui.column().classes('gap-4 item' \
        's-center'):
            ui.button('Login as Job Seeker', 
                     on_click=lambda: login_as_user(dialog)).classes('primary-button w-full')
            ui.button('Login as Company/Vendor', 
                     on_click=lambda: login_as_vendor(dialog)).classes('nav-button w-full')
            ui.button('Cancel', on_click=dialog.close).classes('nav-button w-full')
    
    dialog.open()

def login_as_user(dialog):
    """Navigate to user dashboard"""
    dialog.close()
    ui.navigate.to('/user')

def login_as_vendor(dialog):
    """Navigate to vendor dashboard"""
    dialog.close()
    ui.navigate.to('/vendor')
