from nicegui import ui
import requests
from utils.api import base_url


def show_add_event_page():
    """
    Displays a form to add a new job advertisement.
    Submits the data to the /add_job API endpoint.
    """

    # Header with home link
    with ui.header().classes('items-center justify-between bg-white px-4 py-4 shadow'):
        with ui.row().classes('items-center gap-2'):
            ui.button(icon='home', on_click=lambda: ui.navigate.to('/')).props('flat').classes('text-blue-600')
        ui.label('Add Job Advertisement').classes('text-xl font-bold').style('color:#1976D2')

    # Main container
    with ui.column().classes('w-full min-h-screen items-center bg-gray-100 p-4 md:p-8 lg:p-12'):

        with ui.card().classes('w-full max-w-4xl p-6 shadow-xl rounded-lg bg-white'):

            # --- Input Fields ---
            title = ui.input(label='Job Title', placeholder='e.g., Software Development Trainee') \
                .classes('w-full mb-4')

            description = ui.textarea(label='Job Description', placeholder='Enter detailed job description...') \
                .classes('w-full mb-4')

            location = ui.input(label='Location', placeholder='e.g., Accra, Ghana') \
                .classes('w-full mb-4')

            job_type = ui.select(['On-site', 'Remote', 'Hybrid'], label='Job Type') \
                .classes('w-full mb-4')

            salary = ui.input(label='Salary', placeholder='e.g., GHS 2,500 - 3,500 per month') \
                .classes('w-full mb-4')

            company = ui.input(label='Company Name', placeholder='e.g., MEST Africa') \
                .classes('w-full mb-4')

            logo = ui.input(label='Company Logo URL', placeholder='Paste logo URL here') \
                .classes('w-full mb-4')

            skills = ui.input(
                label='Skills (comma-separated)',
                placeholder='e.g., Python, JavaScript, Django'
            ).classes('w-full mb-4')

            # --- Submit Button ---
            def submit_job():
                payload = {
                    "job_tittle": title.value,
                    "job_description": description.value,
                    "created_ads": location.value, #here was changed to category 
                    # "": job_type.value,
                    "Salaries": salary.value,
                    "category": company.value,
                    "image": logo.value,
                    "Skills": [s.strip() for s in skills.value.split(",")] if skills.value else []
                }

                try:
                    response = requests.post(f"{base_url}/add_job", json=payload)
                    if response.status_code == 201:
                        ui.notify('Job successfully added!', type='positive')
                        ui.navigate.to('/all-ads')
                    else:
                        ui.notify(f"Error: {response.text}", type='negative')
                except Exception as e:
                    ui.notify(f"Failed to connect: {e}", type='negative')

            ui.button('Submit Job', on_click=submit_job).classes(
                'mt-6 bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg'
            )
