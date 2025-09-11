from nicegui import ui
import datetime

# The job advertisement data for MEST Africa
# In a real application, this would come from a database query
MEST_ADVERTISEMENTS = {
    '1': {
        'company': 'Mest Africa',
        'verified': True,
        'logo': 'https://tse4.mm.bing.net/th/id/OIP.pslKeE6ElqR_o2DBg6JaNwAAAA?r=0&cb=ucfimg2&pid=ImgDet&ucfimg=1&w=150&h=150&c=7&dpr=1.5&o=7&rm=3',
        'title': 'Software Development Trainee',
        'location': 'Accra, Ghana',
        'type': 'Hybrid',
        'date_posted': '4 hours ago',
        'status': 'Not applied',
        'description': 'Mest Africa is hiring recent graduates from their program. They are looking for about 25 web development trainees for a hybrid role.',
        'skills': ['Python', 'JavaScript', 'Django'],
    }
}

# The main page for the MEST Africa vendor dashboard
def vendor_dashboard_page():
    # --- Header Section ---
    with ui.header().classes('items-center justify-between'):
        # Left side buttons
        with ui.row().classes('items-center gap-2'):
            ui.button(icon='home', on_click=lambda: ui.navigate.to('/')).classes('text-white')
            ui.button('All Advertisements', on_click=lambda: ui.navigate.to('/all-ads')).classes('text-white')

        # Center section with company info and "Post" button
        with ui.row().classes('items-center gap-4'):
            ui.image('https://tse4.mm.bing.net/th/id/OIP.pslKeE6ElqR_o2DBg6JaNwAAAA?r=0&cb=ucfimg2&pid=ImgDet&ucfimg=1&w=150&h=150&c=7&dpr=1.5&o=7&rm=3').classes('w-12 h-12 rounded-full border border-gray-300 object-contain')
            ui.label('MEST Africa').classes('text-white text-xl font-bold')
            ui.button('Post', icon='post_add', on_click=lambda: ui.navigate.to('/add_event')).classes('bg-green-500 hover:bg-green-600 text-white font-bold')

    # --- Hero Section / Job Listings ---
    with ui.column().classes('w-full mt-12 px-4 md:px-12 lg:px-24 items-center'):
        ui.label('Your Job Advertisements').classes('text-3xl font-bold text-gray-800 mb-6')
        
        # Display the list of advertisements
        for ad_id, ad in MEST_ADVERTISEMENTS.items():
            with ui.card().classes('w-full my-2 p-4 shadow-md rounded-lg border-l-4 border-orange-500 hover:bg-gray-50 transition-colors duration-200 cursor-pointer'):
                with ui.row().classes('w-full items-center justify-between'):
                    # Company Logo and Info
                    with ui.row().classes('items-center gap-4'):
                        ui.image(ad['logo']).classes('w-12 h-12 rounded-full border border-gray-300 object-contain')
                        with ui.column():
                            ui.label(ad['title']).classes('text-lg font-bold')
                            with ui.row().classes('items-center text-sm text-gray-600 space-x-1'):
                                ui.label(ad['company']).classes('font-semibold')
                                ui.label(f'• {ad["location"]} • {ad["type"]}')
                                if ad['verified']:
                                    ui.icon('verified').classes('text-blue-500 text-sm')
                                    ui.label('Verified').classes('text-blue-500 text-sm')
                    
                    # Status label and bookmark icon
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('bookmark_border').classes('text-gray-500 text-xl cursor-pointer')
                        ui.badge(ad['status']).classes('bg-yellow-200 text-yellow-800 px-2 py-1 rounded-full text-xs')
                
                # Description and skills
                ui.label(ad['description']).classes('text-sm text-gray-700 mt-2')
                with ui.row().classes('mt-2 flex-wrap gap-1'):
                    for skill in ad['skills']:
                        ui.badge(skill).classes('bg-gray-200 text-gray-800 text-xs px-2 py-1 rounded-full')
                
                # Edit and Delete buttons
                with ui.row().classes('w-full mt-4 justify-end gap-2'):
                    ui.button('View', on_click=lambda: ui.navigate.to('/edit_event')).classes('bg-blue-500 hover:bg-blue-600 text-white font-bold')
                    ui.button('Edit', on_click=lambda: ui.navigate.to('/edit_event')).classes('bg-blue-500 hover:bg-blue-600 text-white font-bold')
                    ui.button('Delete', on_click=lambda: ui.notify('Job advertisement deleted.', type='positive')).classes('bg-red-500 hover:bg-red-600 text-white font-bold')
                    
