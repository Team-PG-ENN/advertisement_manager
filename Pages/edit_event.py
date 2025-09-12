from nicegui import ui

# Sample data for a job advertisement
job_data = {
    'title': 'Senior Software Engineer',
    'company': 'Tech Solutions Inc.',
    'location': 'Remote',
    'salary': '$120,000 - $150,000',
    'description': 'We are looking for a highly skilled and motivated Senior Software Engineer to join our growing team. The ideal candidate will have extensive experience in Python and cloud technologies.'
}

# The main function to set up the UI
@ui.page('/')
def show_edit_event_page():
    ui.add_head_html("""
        <style>
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem;
            }
            .form-title {
                font-size: 2.25rem;
                font-weight: 700;
                text-align: center;
                margin-bottom: 2rem;
            }
            .form-section {
                margin-bottom: 1.5rem;
            }
            .label {
                font-size: 0.875rem;
                font-weight: 600;
                color: #4b5563;
                margin-bottom: 0.5rem;
                display: block;
            }
            .input {
                width: 100%;
                padding: 0.75rem;
                border-radius: 0.375rem;
                border: 1px solid #d1d5db;
                outline: none;
                transition: border-color 0.2s;
            }
            .input:focus {
                border-color: #3b82f6;
            }
            .textarea {
                min-height: 150px;
            }
            .button {
                width: 100%;
                background-color: #2563eb;
                color: white;
                font-weight: 700;
                padding: 0.75rem;
                border-radius: 0.375rem;
                cursor: pointer;
                border: none;
                transition: background-color 0.2s;
            }
            .button:hover {
                background-color: #1d4ed8;
            }
        </style>
    """)

    with ui.card().classes('w-full container bg-white shadow-lg rounded-xl'):
        ui.label('Edit Job Advertisement').classes('form-title text-gray-800')

        with ui.column().classes('w-full'):
            # Job Title input field
            ui.label('Job Title').classes('label')
            title_input = ui.input(value=job_data['title'], label='Job Title').classes('input')

            # Company input field
            ui.label('Company').classes('label')
            company_input = ui.input(value=job_data['company'], label='Company').classes('input')

            # Location input field
            ui.label('Location').classes('label')
            location_input = ui.input(value=job_data['location'], label='Location').classes('input')

            # Salary input field
            ui.label('Salary').classes('label')
            salary_input = ui.input(value=job_data['salary'], label='Salary').classes('input')

            # Job Description text area
            ui.label('Job Description').classes('label')
            description_textarea = ui.textarea(value=job_data['description'], label='Job Description').classes('input textarea')

            # Save button
            ui.button('Save Changes', on_click=lambda: save_changes()).classes('button mt-4')

    def save_changes():
        # This function would handle saving the updated data
        # For this example, we'll just print the new values
        ui.notify('Changes saved!', type='positive')
        print("Updated Job Data:")
        print(f"Title: {title_input.value}")
        print(f"Company: {company_input.value}")
        print(f"Location: {location_input.value}")
        print(f"Salary: {salary_input.value}")
        print(f"Description: {description_textarea.value}")

