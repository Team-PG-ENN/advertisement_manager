from nicegui import ui
import requests
from utils.api import base_url

ADVERTISEMENTS = {
    1: {
        'company': 'Mest Africa',
        'verified': True,
        'logo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz-M84bN6-c22m_x9rEw83q4f-d_v-6e44XQ&s',
        'title': 'Software Development Trainee',
        'location': 'Accra, Ghana',
        'type': 'Hybrid',
        'salary': 'GHS 2,500 - 3,500 per month',
        'date_posted': '4 hours ago',
        'description': (
            'Mest Africa is looking for recent graduates for a software development trainee role. '
            'This is a hybrid position in our Accra office, focusing on building skills in Python '
            'and JavaScript for full-stack web development. Trainees will work on real-world projects, '
            'receive mentorship from senior developers, and get hands-on experience with modern frameworks like Django. '
            'The program is designed to launch a successful career in tech.'
        ),
        'skills': ['Python', 'JavaScript', 'Django'],
    },
    2: {
        'company': 'Blossom Academy',
        'verified': True,
        'logo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ0x9y4J2k5g_2S1-B-bX7Q4D-J3k-1K7F-g&s',
        'title': 'Data Science Fellowship',
        'location': 'Kumasi, Ghana',
        'type': 'On-site',
        'salary': 'GHS 2,000 - 3,000 per month',
        'date_posted': 'Yesterday',
        'description': (
            'A 6-month fellowship focused on practical data science projects and mentorship. '
            'Fellows will work with real-world datasets, apply machine learning algorithms, '
            'and build predictive models. The program includes workshops, case studies, and a final capstone project. '
            'This is an excellent opportunity for individuals passionate about data to kickstart their career.'
        ),
        'skills': ['Data Analysis', 'Machine Learning', 'SQL'],
    },
    3: {
        'company': 'Soronko Academy',
        'verified': True,
        'logo': 'https://soronkoacademy.org/wp-content/uploads/2021/05/logo-color-1.png',
        'title': 'Web Development Bootcamp',
        'location': 'Accra, Ghana',
        'type': 'Remote',
        'salary': 'GHS 1,500 - 2,500 per month',
        'date_posted': '3 days ago',
        'description': (
            'Intensive bootcamp to become a full-stack web developer. '
            'Focus on MERN stack (MongoDB, Express.js, React, Node.js) and agile methodologies. '
            'The curriculum covers everything from front-end design to back-end logic, '
            'with hands-on coding exercises and portfolio-building projects.'
        ),
        'skills': ['React', 'Node.js', 'MongoDB'],
    },
    4: {
        'company': 'Azubi Africa',
        'verified': True,
        'logo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6-o3F9t3p3g_9f_1-Q2wJ-4-f_5k-5u5i-g&s',
        'title': 'Digital Marketing Specialist',
        'location': 'Takoradi, Ghana',
        'type': 'Hybrid',
        'salary': 'GHS 2,000 - 3,000 per month',
        'date_posted': '2025-09-05',
        'description': (
            'Join our team to manage digital campaigns and SEO strategies. '
            'Gain hands-on experience in a fast-paced environment and contribute to our online presence. '
            'Responsibilities include content creation, social media management, and performance analysis.'
        ),
        'skills': ['SEO', 'SEM', 'Social Media Marketing'],
    },
}

# The page definition for viewing job details

def show_view_event_page(job_id):
    response = requests.get(f"{base_url}/find_job/{job_id}")
    json_data = response.json()
    # Convert job_id from string to int
    ad = json_data["advert"]

    # Header with home link
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    with ui.header().classes('items-center justify-between bg-white px-4 py-4 shadow items-center pr-5 pl-5'):
        with ui.row().classes('items-center gap-2'):
            ui.button(text="< Back",icon='Home',on_click=lambda:ui.navigate.back()).classes('text-white text-center justify-center flex')
        ui.label('Job Details').classes('text-xl font-bold').style('color:#1976D2')

    if ad:
        # Main container with responsive padding and background
        with ui.column().classes('w-full h-full items-center bg-gray-100 p-4 md:p-8 lg:p-12'):
            # Job details card
            with ui.card().classes('w-full h-full max-w-4xl p-6 shadow-xl rounded-lg bg-white'):
                # Header section
                with ui.row().classes('w-full items-center gap-4 border-b pb-4 mb-4'):
                    ui.image(ad['image']).classes('w-20 h-20 rounded-full border border-gray-300 object-contain')
                    with ui.column().classes('flex-grow'):
                        with ui.row().classes('items-center gap-2'):
                            ui.label(ad['job_title']).classes('text-2xl font-bold text-gray-800')
                        #     if job_ad['verified']:
                        #         ui.tooltip('Verified Partner')
                        #         ui.icon('verified').classes('text-blue-500')
                        # ui.label(job_ad['company']).classes('text-xl text-gray-600')

                # Main content section with detailed information
                with ui.column().classes('w-full'):
                    # Job metadata (location, type, salary)
                    with ui.row().classes('w-full flex-wrap gap-x-6 gap-y-2 mb-4'):
                        with ui.column().classes('flex-grow'):
                            ui.label('Location').classes('text-sm font-semibold text-gray-500')
                            ui.label(ad['job_title']).classes('text-lg')
                        # with ui.column().classes('flex-grow'):
                        #     ui.label('Job Type').classes('text-sm font-semibold text-gray-500')
                        #     ui.label(job_ad['type']).classes('text-lg')
                        # with ui.column().classes('flex-grow'):
                        #     ui.label('Salary').classes('text-sm font-semibold text-gray-500')
                        #     ui.label(ad['salary']).classes('text-lg text-green-600 font-bold')
                    
                    # Detailed description
                    ui.label('Job Description').classes('text-lg font-bold mt-4 mb-2')
                    ui.label(ad['job_description']).classes('text-base text-gray-700 leading-relaxed')

                    # Skills section
                    ui.label('Skills').classes('text-lg font-bold mt-4 mb-2')
                    with ui.row().classes('w-full flex-wrap gap-2'):
                        for skill in ad['skills']:
                            ui.badge(skill).classes('bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm font-medium')
                    
                    # Application selector
                    def handle_application_choice(e):
                        if e.value == 'Apply':
                            ui.notify('You have chosen to apply for this job!')
                        elif e.value == 'Get in touch':
                            ui.notify('You have chosen to get in touch with the company.')

                    ui.select(
                        ['Apply', 'Get in touch'],
                        on_change=handle_application_choice,
                        label="Application Options"
                    ).classes('w-full mt-6')

    else:
        # Display an error message if the job is not found
        with ui.column().classes('w-full h-screen items-center justify-center'):
            ui.label('Job Not Found').classes('text-4xl font-bold text-red-600')
            ui.label('The requested job advertisement does not exist.').classes('text-lg mt-2')
            ui.button('Go to Homepage', on_click=lambda: ui.navigate.to('/')).classes('mt-6')



















# from nicegui import ui
# import requests
# from utils.api import base_url


# def show_edit_event_page(job_id: int):
#     """
#     Displays a form to edit an existing job advertisement.
#     Submits updated data to the /update_job/{job_id} API endpoint.
#     """

#     # Fetch existing job data
#     try:
#         response = requests.get(f"{base_url}/find_job/{job_id}")
#         if response.status_code == 200:
#             job_ad = response.json().get("advert", {})
#         else:
#             job_ad = {}
#     except Exception as e:
#         job_ad = {}
#         ui.notify(f"Error fetching job: {e}", type='negative')

#     # Header
#     with ui.header().classes('items-center justify-between bg-white px-4 py-4 shadow'):
#         with ui.row().classes('items-center gap-2'):
#             ui.button(icon='home', on_click=lambda: ui.navigate.to('/')).props('flat').classes('text-blue-600')
#         ui.label('Edit Job Advertisement').classes('text-xl font-bold').style('color:#1976D2')

#     if not job_ad:
#         with ui.column().classes('w-full h-screen items-center justify-center'):
#             ui.label('Job Not Found').classes('text-3xl font-bold text-red-600')
#             ui.button('Go to Homepage', on_click=lambda: ui.navigate.to('/')).classes('mt-6')
#         return

#     # Main container
#     with ui.column().classes('w-full min-h-screen items-center bg-gray-100 p-4 md:p-8 lg:p-12'):

#         with ui.card().classes('w-full max-w-4xl p-6 shadow-xl rounded-lg bg-white'):

#             # --- Pre-filled Input Fields ---
#             title = ui.input(label='Job Title', value=job_ad.get("Title", "")) \
#                 .classes('w-full mb-4')

#             description = ui.textarea(label='Job Description', value=job_ad.get("Description", "")) \
#                 .classes('w-full mb-4')

#             location = ui.input(label='Location', value=job_ad.get("Location", "")) \
#                 .classes('w-full mb-4')

#             job_type = ui.select(['On-site', 'Remote', 'Hybrid'],
#                                  value=job_ad.get("Type", None),
#                                  label='Job Type') \
#                 .classes('w-full mb-4')

#             salary = ui.input(label='Salary', value=job_ad.get("Salary", "")) \
#                 .classes('w-full mb-4')

#             company = ui.input(label='Company Name', value=job_ad.get("Company", "")) \
#                 .classes('w-full mb-4')

#             logo = ui.input(label='Company Logo URL', value=job_ad.get("Logo", "")) \
#                 .classes('w-full mb-4')

#             skills = ui.input(
#                 label='Skills (comma-separated)',
#                 value=", ".join(job_ad.get("Skills", [])) if job_ad.get("Skills") else ""
#             ).classes('w-full mb-4')

#             # --- Submit Button ---
#             def submit_update():
#                 payload = {
#                     "Title": title.value,
#                     "Description": description.value,
#                     "Location": location.value,
#                     "Type": job_type.value,
#                     "Salary": salary.value,
#                     "Company": company.value,
#                     "Logo": logo.value,
#                     "Skills": [s.strip() for s in skills.value.split(",")] if skills.value else [],
#                 }

#                 try:
#                     response = requests.put(f"{base_url}/update_job/{job_id}", json=payload)
#                     if response.status_code == 200:
#                         ui.notify('Job successfully updated!', type='positive')
#                         ui.navigate.to(f'/view_event/{job_id}')
#                     else:
#                         ui.notify(f"Error: {response.text}", type='negative')
#                 except Exception as e:
#                     ui.notify(f"Failed to connect: {e}", type='negative')

#             ui.button('Update Job', on_click=submit_update).classes(
#                 'mt-6 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg'
#             )
