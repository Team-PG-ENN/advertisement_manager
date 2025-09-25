from nicegui import ui, run, app
import requests
from utils.api import base_url


_add_event_btn:ui.button = None

def _run_add_event(data, files, token):
    return requests.post(
        f"{base_url}/adverts", 
        data=data,
          files=files,
          headers={"Authorization": f"Bearer {token}"},
          )
_event_image = None

def _handle_image_upload(event):
  global _event_image
  _event_image = event.content
   
  async def _add_event(data, files):
    _add_event_btn.props(add="disable loading") 
    response = await run.cpu_bound(_run_add_event, data, files, app.storage.user.get("access_token"))
    print(response.status_code, response.content)
    _add_event_btn.props(remove="disable loading")


def show_add_event_page():
    ui.query('.nicegui-content').classes('p-0 m-0 gap-0')

    with ui.column().classes('w-full min-h-screen items-center p-0 m-0 bg-[url("/assets/signupimage.png")] md:p-8 lg:p-12 bg-cover bg-center'):
        ui.element("div").classes("absolute inset-0 bg-black/40")

        with ui.card().classes('w-full max-w-4xl p-6 items-center shadow-xl rounded-lg bg-white'):
            ui.label('Add New Advertisement').classes('text-xl items-center  justify-center text-black font-bold').style
            # --- Job Title ---
            with ui.element("div").classes("flex flex-col w-full py-2"):
                ui.label("Job Title").classes("text-xs text-left py-2")
                job_title = ui.input(
                    placeholder="Enter job title"
                ).props("flat outlined dense").classes("rounded-sm bg-white text-xs")

            # --- Job Description ---
            with ui.element("div").classes("flex flex-col w-full py-2"):
                ui.label("Job Description").classes("text-xs text-left py-2")
                job_description = ui.textarea(
                    placeholder="Enter job description"
                ).props("outlined dense").classes("bg-white text-xs")

            # --- Salary + Category (same row) ---
            with ui.element("div").classes("flex w-full flex-row gap-4 py-2"):
                with ui.element("div").classes("flex flex-col w-[49%]"):
                    ui.label("Price/Salary").classes("text-xs text-left py-2")
                    job_salary = ui.input(
                        placeholder="e.g. ₡100,000 - ₡140,000"
                    ).props("flat outlined dense").classes("bg-white text-xs")

                with ui.element("div").classes("flex flex-col w-[49%]"):
                    ui.label("Category").classes("text-xs text-left py-2")
                    job_category = ui.select(
                        ["Data Analytics", "Web Development", "Data Science", "Cloud Computing", "Others"],
                        with_input=True,
                    ).props("outlined dense label='Select a category'").classes("bg-white text-xs")

            # --- Job Type + Location (same row) ---
            with ui.element("div").classes("flex w-full flex-row gap-4 py-2"):
                with ui.element("div").classes("flex flex-col w-[49%]"):
                    ui.label("Job Type").classes("text-xs text-left py-2")
                    job_type = ui.select(
                        ["On-site", "Remote", "Hybrid"],
                    ).props("outlined dense label='Select a job type'").classes("bg-white text-xs")

                with ui.element("div").classes("flex flex-col w-[49%]"):
                    ui.label("Location").classes("text-xs text-left py-2")
                    job_location = ui.input(
                        placeholder="e.g. Accra, Kumasi"
                    ).props("flat outlined dense").classes("bg-white text-xs")

            # --- Skills full width ---
            with ui.element("div").classes("flex flex-col w-full py-2"):
                ui.label("Skills (comma-separated)").classes("text-xs text-left py-2")
                job_skills = ui.input(
                    placeholder="e.g. React, Node.js, SQL"
                ).props("flat outlined dense").classes("bg-white text-xs")

            # --- Company Name ---
            with ui.element("div").classes("flex flex-col w-full py-2"):
                ui.label("Company Name").classes("text-xs text-left py-2")
                company_name = ui.input(
                    placeholder="Enter company name"
                ).props("flat outlined dense").classes("bg-white text-xs")

            # --- Company Logo URL ---
            with ui.element("div").classes("flex flex-col w-full py-2"):
                ui.label("Company Logo URL").classes("text-xs text-left py-2")
                company_logo = ui.input(
                    placeholder="Paste company logo image URL"
                ).props("flat outlined dense").classes("bg-white text-xs")

            # --- Submit Button ---
            with ui.element("div").classes("w-full flex items-center justify-center py-4"):
                def submit_job():
                    payload = {
                        "job_title": job_title.value,
                        "job_description": job_description.value,
                        "salaries": job_salary.value,
                        "category": job_category.value,
                        "job_type": job_type.value,
                        "location": job_location.value,
                        "company": company_name.value,
                        "image": company_logo.value,
                        "skills": [s.strip() for s in job_skills.value.split(",")] if job_skills.value else [],
                    }

                    try:
                        response = requests.post(f"{base_url}/add_job", json=payload)
                        if response.status_code == 201:
                            ui.notify("Job successfully created!", type="positive")
                            ui.navigate.to("/all-ads")
                        else:
                            ui.notify(f"Error: {response.text}", type="negative")
                    except Exception as e:
                        ui.notify(f"Failed to connect: {e}", type="negative")

                ui.button(
                    "Add New Job",
                    on_click=submit_job
                ).classes("mt-6 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 ml-auto")








# def show_add_event_page():
#     """
#     Displays a form to add a new job advertisement.
#     Submits the data to the /add_job API endpoint.
#     """

#     # # Header with home link
#     # with ui.header().classes('items-center justify-between bg-white px-4 py-4 shadow'):
#     #     with ui.row().classes('items-center gap-2'):
#     #         ui.button(icon='home', on_click=lambda: ui.navigate.to('/')).props('flat').classes('text-blue-600')
#     #     ui.label('Add Job Advertisement').classes('text-xl font-bold').style('color:#1976D2')

#     # Main container
#     ui.query('.nicegui-content').classes('p-0 m-0 gap-0')
#     with ui.column().classes('w-full min-h-screen items-center p-0 m-0 bg-[url("/assets/signupimage.png")] md:p-8 lg:p-12 bg-cover bg-center'):
#         ui.element("div").classes("absolute inset-0 bg-black/40")

#         with ui.card().classes('w-full max-w-4xl p-6 shadow-xl rounded-lg bg-white'):
#             ui.label('Add Job Advertisement').classes('text-xl items-center  justify-center text-black font-bold').style
#             # --- Input Fields ---
#             title = ui.input(label='Job Title', placeholder='e.g., Software Development Trainee') \
#                 .classes('w-full mb-4')

#             description = ui.textarea(label='Job Description', placeholder='Enter detailed job description...') \
#                 .classes('w-full mb-4')

#             location = ui.input(label='Location', placeholder='e.g., Accra, Ghana') \
#                 .classes('w-full mb-4')

#             job_type = ui.select(['On-site', 'Remote', 'Hybrid'], label='Job Type') \
#                 .classes('w-full mb-4')

#             salary = ui.input(label='Salary', placeholder='e.g., GHS 2,500 - 3,500 per month') \
#                 .classes('w-full mb-4')

#             company = ui.input(label='Company Name', placeholder='e.g., MEST Africa') \
#                 .classes('w-full mb-4')

#             logo = ui.input(label='Company Logo URL', placeholder='Paste logo URL here') \
#                 .classes('w-full mb-4')

#             skills = ui.input(
#                 label='Skills (comma-separated)',
#                 placeholder='e.g., Python, JavaScript, Django'
#             ).classes('w-full mb-4')

#             # --- Submit Button ---
#             def submit_job():
#                 payload = {
#                     "job_title": title.value,
#                     "job_description": description.value,
#                     "created_at": location.value, #here was changed to category 
#                     "salaries": salary.value,
#                     "category": company.value,
#                     "image": logo.value,
#                     "skills": [s.strip() for s in skills.value.split(",")] if skills.value else []
#                 }

#                 try:
#                     response = requests.post(f"{base_url}/add_job", json=payload)
#                     if response.status_code == 201:
#                         ui.notify('Job successfully added!', type='positive')
#                         ui.navigate.to('/all-ads')
#                     else:
#                         ui.notify(f"Error: {response.text}", type='negative')
#                 except Exception as e:
#                     ui.notify(f"Failed to connect: {e}", type='negative')

#             ui.button('Submit Job', on_click=submit_job).classes(
#                 'mt-6 bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg'
#             )
