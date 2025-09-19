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
    with ui.header().classes('bg-white px-4 py-4 shadow items-center'):
        with ui.row().classes('w-full flex justify-between items-center pr-5 pl-5'):

            # --- Left Section (Home link) ---
            with ui.row().classes('items-center gap-2'):
                ui.link('Home', target='/').classes(
                    'no-underline font-bold hover:underline text-base md:text-xl'
                ).style('color: #1976D2;')

            # --- Center Section 
            with ui.row().classes('items-center gap-3 text-center border px-2'):

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
                ui.button('Add Job', icon='post_add',
                    on_click=lambda: ui.navigate.to('/add_event')
                ).classes(
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
    with ui.row().classes('w-full mt-12 px-4 md:px-12 lg:px-24 flex-wrap justify-center'):
        # Main container for the job ads list
        with ui.column().classes('w-full lg:w-3/5 xl:w-1/2'):
            ui.label('Posted Advertisments').classes('text-2xl font-bold text-gray-800 mb-6')
            
            # A list of advertisement data
            advertisements = json_data["adverts"]

            # Function to handle button clicks and navigate
            def view_details(job_id):
                ui.navigate.to(f'/view_event?id={job_id}')

            # Loop to create each job advertisement card
            for ad in advertisements:
                with ui.card().classes('w-full my-2 p-2 shadow-md rounded-lg border-l-4 border-orange-500 hover:bg-gray-50 transition-colors duration-200 cursor-pointer flex-row items-center'):
                    # Company Logo
                    ui.image(ad['image']).classes('w-12 h-12 rounded-full border border-gray-300 object-contain flex-shrink-0')
                    
                    # Middle section with job details
                    with ui.column().classes('flex-grow px-4'):
                        with ui.row().classes('items-center gap-2'):
                            ui.label(ad['job_title']).classes('text-lg font-bold')
                            with ui.element("div"):
                                ui.tooltip('Verified Partner')
                                ui.icon('verified').classes('text-blue-500 text-sm')
                                ui.label('Verified').classes('text-blue-500 text-sm')
                        
                        # Tightly packed company, location, and date
                        with ui.row().classes('items-center text-sm text-gray-600 space-x-1'):
                            
                            # ui.label(f'• {ad["location"]}')
                            # ui.label(f'• {ad["type"]}')
                            ui.label(f'• {ad["created_at"]}').classes('text-xs text-gray-500')
                        
                        ui.label(ad['job_description']).classes('text-sm text-gray-700 mt-1')

                        # Skills list
                        with ui.row().classes('mt-2 flex-wrap gap-1'):
                            for skill in ad['skills']:
                                ui.badge(skill).classes('bg-gray-200 text-gray-800 text-xs px-2 py-1 rounded-full')
                        
                #     # View Details button to the right, with bookmark icon
                #     with ui.column().classes('flex-shrink-0 items-center gap-2'):
                #         ui.icon('bookmark_border').classes('text-gray-500 text-xl cursor-pointer')
                #         # ui.button('View', on_click=lambda id=ad['_id']: view_details(id)).classes('bg-orange-500 hover:bg-orange-600 text-white font-bold')
                # def confirm_delete(job_id):
                #     """Open a confirmation dialog before deleting a job."""
                #     with ui.dialog() as dialog, ui.card().classes('p-6'):
                #         ui.label('Are you sure you want to delete this job?').classes('text-lg font-bold mb-4')

                #         with ui.row().classes('gap-4 justify-end'):
                #             ui.button('Cancel', on_click=dialog.close).props('color=grey')
                #             ui.button('Yes, Delete', on_click=lambda: delete_job(job_id, dialog)).props('color=negative')


                # def delete_job(job_id, dialog):
                #     """Perform delete request and refresh UI after deletion."""
                #     try:
                #         response = requests.delete(f"{base_url}/delete_job/{job_id}")
                #         if response.status_code == 200:
                #             ui.notify('Job advertisement deleted successfully.', type='positive')
                #             dialog.close()
                #             # Refresh vendor and homepage listings
                #             vendor_dashboard_page()
                #         else:
                #             ui.notify(f'Failed to delete job: {response.text}', type='negative')
                #     except Exception as e:
                #         ui.notify(f'Error: {e}', type='negative')

                def delete_job(job_id):
                    response = requests.delete(f"{base_url}/delete_job/{job_id}")
                    if response.status_code == 200:
                        ui.notify('Job advertisement deleted.', type='positive')
                        ui.navigate.reload()

                # Edit and Delete buttons
                with ui.row().classes('w-full mt-1 justify-end gap-2'):
                    ui.button('View', on_click=lambda id=ad['_id']: view_details(id)).classes('bg-blue-500 hover:bg-blue-600 text-white font-bold')
                    ui.button('Edit', on_click=lambda: ui.navigate.to('/edit_event/{event_id}')).classes('bg-blue-500 hover:bg-blue-600 text-white font-bold')
                    ui.button('Delete', color="red",on_click=lambda id=ad['_id']: delete_job(id)).classes('bg-red-500 hover:bg-red-600 text-white font-bold')
                    
