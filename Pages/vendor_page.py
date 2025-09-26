from nicegui import ui
import datetime
import requests
from utils.api import base_url
from functools import partial



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

    response = requests.get(f"{base_url}/view_job")
    json_data = response.json()
    # --- Header Section ---
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    with ui.header().classes('bg-white px-4 py-4 shadow items-center'):
        with ui.row().classes('w-full flex justify-between items-center pr-5 pl-5'):

            # --- Left Section (Home link) ---
            with ui.row().classes('items-center gap-2'):
                ui.link('Back to Homepage', target='/').classes(
                    'no-underline font-bold hover:underline text-base md:text-lg'
                ).style('color: #1976D2;')

            # --- Center Section 
            with ui.row().classes('items-center gap-3 text-center px-2'):

                ui.image(
                    'https://tse4.mm.bing.net/th/id/OIP.pslKeE6ElqR_o2DBg6JaNwAAAA?r=0&cb=ucfimg2&pid=ImgDet&ucfimg=1&w=150&h=150&c=7&dpr=1.5&o=7&rm=3'
                ).classes('w-10 h-10 md:w-12 md:h-12  border border-gray-300 ')

                ui.label('MEST Africa').classes(
                    'text-gray-800 text-base md:text-xl font-bold'
                )  
            
                ui.link('All Advertisements', target='/all-ads').classes(
                'ml-5 no-underline font-bold hover:underline text-base md:text-xl').style('color: #1976D2;')

            # --- Right Section (Post button) ---
            with ui.row().classes('items-center'):
                ui.button('Add a Job', icon='post_add',
                    on_click=lambda: ui.navigate.to('/add_event')
                ).props('no-caps').classes(
                    ' hover:bg-green-600 text-white font-bold rounded px-4 md:px-6'
                )

    # --- Hero Section / Job Listings ---ui.label(ad['company']).classes('font-semibold')
    # with ui.column().classes('w-full mt-12 px-4 md:px-12 lg:px-24 items-center'):
    #     ui.label('Your Job Advertisements').classes('text-3xl font-bold text-gray-800 mb-6')
        
        # # Display the list of advertisements
        # for ad_id, ad in MEST_ADVERTISEMENTS.items():
        #     with ui.card().classes('w-full my-2 p-4 shadow-md rounded-lg border-l-4 border-orange-500 hover:bg-gray-50 transition-colors duration-200 cursor-pointer'):
        #         # with ui.row().classes('w-full items-center justify-between'):
        #             # Company Logo and Info
        #             # with ui.row().classes('items-center gap-4'):
        #             #     ui.image(ad['logo']).classes('w-12 h-12 rounded-full border border-gray-300 object-contain')
        #                 with ui.column():
        #                     ui.label(ad['Title']).classes('text-lg font-bold')
        #                     with ui.row().classes('items-center text-sm text-gray-600 space-x-1'):
        #                         ui.label(ad['company']).classes('font-semibold')
        #                         # ui.label(f'• {ad["location"]} • {ad["type"]}')
        #                         # if ad['verified']:
        #                         #     ui.icon('verified').classes('text-blue-500 text-sm')
        #                         #     ui.label('Verified').classes('text-blue-500 text-sm')
                    
        #             # # Status label and bookmark icon
        #             # with ui.row().classes('items-center gap-2'):
        #             #     ui.icon('bookmark_border').classes('text-gray-500 text-xl cursor-pointer')
        #             #     ui.badge(ad['status']).classes('bg-yellow-200 text-yellow-800 px-2 py-1 rounded-full text-xs')
                
        #         # # Description and skills
        #         # ui.label(ad['description']).classes('text-sm text-gray-700 mt-2')
        #         # with ui.row().classes('mt-2 flex-wrap gap-1'):
        #         #     for skill in ad['skills']:
        #         #         ui.badge(skill).classes('bg-gray-200 text-gray-800 text-xs px-2 py-1 rounded-full')
                
        #         def view_details(job_id):
        #             ui.navigate.to(f'/view_event?id={job_id}')
    # --- Advertisements Section ---
    with ui.row().classes('md:w-full px-4 md:px-10 lg:px-24 flex-wrap bg-gray-100 justify-center'):
        with ui.column().classes('w-full my-5'):
            ui.label('Advertisements Summary').classes('text-2xl md:mt-5 font-bold text-gray-800')
            with ui.row().classes('w-full'):
                with ui.card().classes('md:w-[20%] w-full bg-white'):
                    ui.label('Total Adverts')
                    ui.label(2).classes('text-3xl font-bold')
                with ui.card().classes('md:w-[78%] bg-white'):
                    ui.label('Advert Categories').classes('p-0 m-0')
                    with ui.row().classes('w-full gap-2 flex-wrap'):
                        for cat in ['Web Development', 'Data Analytics', 'Digital Marketing','Cloud Computing','Software Engineering','Project Management']:
                            ui.button(cat).props('no-caps flat').classes(
                                "rounded-full bg-blue-100 text-black px-3 py-1 hover:bg-blue-200"
                            )
        # Main container for the job ads list
        with ui.column().classes('w-full my-5'):
            ui.label('Posted Adverts').classes('text-2xl font-bold text-gray-800')

            # A list of advertisement data
            advertisements = json_data["adverts"]

            # Function to handle button clicks and navigate
            def view_details(job_id):
                ui.navigate.to(f'/view_event?id={job_id}')

            # Loop to create each job advertisement card
            for ad in advertisements:
                with ui.card().classes(
                    'w-full my-2 px-5 py-3 shadow-md rounded-lg border-l-4 border-orange-400 hover:bg-gray-50 transition-colors duration-200 cursor-pointer'
                ):
                    with ui.row().classes('items-center w-full'):
                        # Company Logo
                        ui.image(ad['image']).classes(
                            'w-12 h-12 rounded-full border border-gray-300 object-contain flex-shrink-0'
                        )
                        
                        # Middle section with job details
                        with ui.column().classes('flex-grow px-4'):
                            with ui.row().classes('items-center gap-2'):
                                ui.label(ad['job_title']).classes('text-lg font-bold')
                                with ui.row().classes('gap-0 p-0 m-0'):
                                    ui.tooltip('Verified Partner')
                                    ui.icon('verified').classes('text-blue-500 text-sm')
                                    ui.label('Verified').classes('text-blue-500 text-sm')
                            
                            # # Company, location, and date
                            # with ui.row().classes('items-center text-sm text-gray-600 space-x-1'):
                            #     ui.label(f'• {ad["created_at"]}').classes('text-xs text-gray-500')
                            
                            ui.label(ad['job_description']).classes('text-sm text-gray-700 mt-1')

                            # Skills list
                            with ui.row().classes('mt-2 flex-wrap gap-1'):
                                for skill in ad['skills']:
                                    ui.badge(skill).classes(
                                        'bg-gray-200 text-gray-800 text-xs px-2 py-1 rounded-full'
                                    )

                        def delete_job(job_id): 
                            response = requests.delete(f"{base_url}/delete_job/{job_id}") 
                            if response.status_code == 200: 
                                ui.notify('Job advertisement deleted.', type='positive') 
                                ui.navigate.reload()

                        # Buttons section aligned to the right
                        with ui.row().classes('justify-end items-center gap-2'):
                            ui.button('View', on_click=lambda id=ad['_id']: view_details(id)).props('no-caps flat').classes(
                                'bg-blue-200 hover:bg-blue-300  font-bold px-3 py-1 rounded'
                            )
                            ui.button('Edit', on_click=lambda: ui.navigate.to(f'/edit_event/{ad["_id"]}')).props('no-caps flat').classes(
                                'bg-blue-200 hover:bg-blue-300 font-bold px-3 py-1 rounded'
                            )
                            ui.button('Delete', on_click=lambda id=ad['_id']: delete_job(id)).props('no-caps flat').classes(
                                'bg-red-200 hover:bg-red-300 text-red font-bold px-3 py-1 rounded'
                            )
