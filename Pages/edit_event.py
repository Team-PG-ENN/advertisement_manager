
from nicegui import ui
import requests
from utils.api import base_url


def show_edit_event_page(job_id):
    """
    Displays a form to edit an existing job advertisement.
    Submits updated data to the /update_job/{job_id} API endpoint.
    """

    # Fetch existing job data
    try:
        response = requests.get(f"{base_url}/find_job/{job_id}")
        if response.status_code == 200:
            json_data = response.json()
            job_ad = json_data.get("advert", {})
        else:
            job_ad = {}
    except Exception as e:
        job_ad = {}
        ui.notify(f"Error fetching job: {e}", type='negative')

    # If job not found
    if not job_ad:
        with ui.column().classes('w-full h-screen items-center justify-center'):
            ui.label('Job Not Found').classes('text-3xl font-bold text-red-600')
            ui.button('Go to Homepage', on_click=lambda: ui.navigate.to('/')).classes('mt-6')
        return

    # Main container
    ui.query('.nicegui-content').classes('p-0 m-0 gap-0')
    with ui.column().classes(
        'w-full min-h-screen items-center bg-[url("/assets/signupimage.png")] '
        'md:p-8 lg:p-12 bg-cover bg-center'
    ):
        ui.element("div").classes("absolute inset-0 bg-black/40")

        with ui.card().classes('w-full max-w-4xl p-6 shadow-xl rounded-lg bg-white'):
            ui.label('Edit Job Advertisement').classes('text-xl text-black font-bold mb-4')

            # --- Pre-filled Input Fields ---
            title = ui.input(label='Job Title', value=job_ad.get("job_title", "")).classes('w-full mb-4')

            description = ui.textarea(
                label='Job Description',
                value=job_ad.get("job_description", "")
            ).classes('w-full mb-4 outlined')

            location = ui.input(
                label='Location / Category',
                value=job_ad.get("category", "")
            ).classes('w-full mb-4')

            salary = ui.input(label='Salary', value=job_ad.get("salaries", "")).classes('w-full mb-4')

            company = ui.input(label='Company Name', value=job_ad.get("company", "")).classes('w-full mb-4')

            logo = ui.input(label='Company Logo URL', value=job_ad.get("image", "")).classes('w-full mb-4')

            skills = ui.input(
                label='Skills (comma-separated)',
                value=", ".join(job_ad.get("skills", [])) if job_ad.get("skills") else ""
            ).classes('w-full mb-4')

            # --- Submit Button ---
            def submit_update():
                payload = {
                    "job_title": title.value,
                    "job_description": description.value,
                    "salaries": salary.value,
                    # "category": location.value,
                    # "company": company.value,
                    # "image": logo.value,
                    "skills": [s.strip() for s in skills.value.split(",")] if skills.value else []
                }

                try:
                    update_response = requests.put(f"{base_url}/update_job/{job_id}", json=payload)
                    if update_response.status_code == 200:
                        ui.notify('Job successfully updated!', type='positive')
                        ui.navigate.to('/vendor')
                    else:
                        ui.notify(f"Error: {update_response.text}", type='negative')
                except Exception as e:
                    ui.notify(f"Failed to connect: {e}", type='negative')

            ui.button(
                'Update Job',
                on_click=submit_update
            ).classes('mt-6 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg')
