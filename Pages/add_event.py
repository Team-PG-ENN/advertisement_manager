



from nicegui import ui
import requests
from utils.api import base_url


_job_image = None  # optional image (e.g., company logo or job banner)

def _handle_image_upload(event):
    global _job_image
    _job_image = event.content

def _post_job(data, files):
    response = requests.post(f"{base_url}/jobs", data=data, files=files)
    print(response.status_code, response.content)
    if response.status_code == 200:
        ui.notify("Job posted successfully!", type="positive")
        return ui.navigate.to("/")
    elif response.status_code == 422:
        ui.notify("Please ensure all inputs are filled!", type="negative")
    else:
        ui.notify("Failed to post job. Try again.", type="negative")


@ui.page('/create_job')
def show_add_event_page():
    
    with ui.element("div").classes("w-full h-full items-center flex flex-col bg-slate-100"):
        # "Post Job" section
        ui.label("Post a Job").classes("font-bold text-3xl mb-4 mt-10")
        with ui.card().classes("font-bold shadow-xl w-3/5"):
            # Job Title
            ui.label("Job Title").classes("text-slate-500 font-normal text-sm")
            job_title = ui.input(placeholder="Enter job title").props("outlined").classes("w-full mb-3")

            # Company Name
            ui.label("Company").classes("text-slate-500 font-normal text-sm")
            job_company = ui.input(placeholder="Enter company name").props("outlined").classes("w-full mb-3")

            # Job Location
            ui.label("Location").classes("text-slate-500 font-normal text-sm")
            job_location = ui.input(placeholder="Enter job location").props("outlined").classes("w-full mb-3")

            # Salary
            ui.label("Salary").classes("text-slate-500 font-normal text-sm")
            job_salary = ui.input(placeholder="Enter salary").props("outlined type=number").classes("w-full mb-3")

    # Description + Image upload (optional)
    with ui.element("div").classes("w-full items-center flex flex-col bg-slate-100 mt-10"):
        ui.label("Job Details").classes("font-bold text-3xl mb-4")
        with ui.card().classes("font-bold shadow-xl mb-8 w-3/5"):
            # Image upload (optional)
            ui.label("Company Logo / Job Banner (optional)").classes("text-slate-500 font-normal text-sm")
            ui.upload(label="Click or drop an image", auto_upload=True, on_upload=_handle_image_upload).props("color=green").classes("w-full h-40 bg-slate-200 rounded mb-4")

            # Job Description
            ui.label("Job Description").classes("text-slate-500 font-normal text-sm")
            job_description = ui.input(placeholder="Type job description here...").props("outlined type=textarea").classes("w-full h-32")

        # Post Job Button
        ui.button(
            "Post Job",
            on_click=lambda: _post_job(
                data={
                    "job_title": job_title.value,
                    "category": job_company.value,    #company
                    "skills": job_location.value,   # this was location
                    "salaries": job_salary.value,
                    "job_description": job_description.value
                },
                files={"image": _job_image} if _job_image else {}
            ),
        ).classes("w-3/5 h-12 mb-20 bg-purple-700 hover:bg-purple-800 text-white font-semibold")

    


















# # from nicegui import ui

# # # The main function to set up the UI
# # @ui.page('/')
# # def show_add_event_page():
# #     ui.add_head_html("""
# #         <style>
# #             .container {
# #                 max-width: 800px;
# #                 margin: 0 auto;
# #                 padding: 2rem;
# #             }
# #             .form-title {
# #                 font-size: 2.25rem;
# #                 font-weight: 700;
# #                 text-align: center;
# #                 margin-bottom: 2rem;
# #             }
# #             .form-section {
# #                 margin-bottom: 1.5rem;
# #             }
# #             .label {
# #                 font-size: 0.875rem;
# #                 font-weight: 600;
# #                 color: #4b5563;
# #                 margin-bottom: 0.5rem;
# #                 display: block;
# #             }
# #             .input {
# #                 width: 100%;
# #                 padding: 0.75rem;
# #                 border-radius: 0.375rem;
# #                 border: 1px solid #d1d5db;
# #                 outline: none;
# #                 transition: border-color 0.2s;
# #             }
# #             .input:focus {
# #                 border-color: #3b82f6;
# #             }
# #             .textarea {
# #                 min-height: 150px;
# #             }
# #             .button {
# #                 width: 100%;
# #                 background-color: #2563eb;
# #                 color: white;
# #                 font-weight: 700;
# #                 padding: 0.75rem;
# #                 border-radius: 0.375rem;
# #                 cursor: pointer;
# #                 border: none;
# #                 transition: background-color 0.2s;
# #             }
# #             .button:hover {
# #                 background-color: #1d4ed8;
# #             }
# #         </style>
# #     """)

# #     # Function to be called when the form is submitted
# #     def add_new_job():
# #         # You would typically save this data to a database here.
# #         # For this example, we'll just print the new values and clear the form.
# #         ui.notify('New job advertisement added!', type='positive')
# #         print("New Job Advertisement Data:")
# #         print(f"Title: {title_input.value}")
# #         print(f"Company: {company_input.value}")
# #         print(f"Location: {location_input.value}")
# #         print(f"Salary: {salary_input.value}")
# #         print(f"Description: {description_textarea.value}")
        
# #         # Clear the form fields after submission
# #         title_input.value = ''
# #         company_input.value = ''
# #         location_input.value = ''
# #         salary_input.value = ''
# #         description_textarea.value = ''

# #     with ui.card().classes('w-full container bg-white shadow-lg rounded-xl'):
# #         ui.label('Add New Job Advertisement').classes('form-title text-gray-800')

# #         with ui.column().classes('w-full'):
# #             # Job Title input field, starting empty
# #             ui.label('Job Title').classes('label')
# #             title_input = ui.input(value='', label='Enter job title').classes('input')

# #             # Company input field, starting empty
# #             ui.label('Company').classes('label')
# #             company_input = ui.input(value='', label='Enter company name').classes('input')

# #             # Location input field, starting empty
# #             ui.label('Location').classes('label')
# #             location_input = ui.input(value='', label='Enter job location').classes('input')

# #             # Salary input field, starting empty
# #             ui.label('Salary').classes('label')
# #             salary_input = ui.input(value='', label='Enter salary range').classes('input')

# #             # Job Description text area, starting empty
# #             ui.label('Job Description').classes('label')
# #             description_textarea = ui.textarea(value='', label='Enter job description').classes('input textarea')

# #             # Submit button
# #             ui.button('Add Job', on_click=add_new_job).classes('button mt-4')