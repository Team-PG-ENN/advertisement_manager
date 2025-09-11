from nicegui import ui,app
from components.header import show_header
from components.footer import show_footer
from Pages.home import show_home_page
from Pages.add_event import show_add_event_page
from Pages.edit_event import show_edit_event_page
from Pages.view_event import show_view_event_page


# main.py


# Shared storage (imported by edit_event.py)
job_adverts = []
job_id_counter = 1



@ui.page("/")
def home_page():
    show_header()
    show_home_page()
    show_footer()

@ui.page("/add_event")
def add_event_page():
    show_header()
    show_add_event_page()

# @ui.page("/edit_event")
# def edit_event_page():
#     show_header()
#     show_edit_event_page()

@ui.page("/view_event")
def view_event_page():
    show_header()
    show_view_event_page()

# @ui.page("/edit_event/{event_id}")
# def edit_event_page(event_id: int):
#     show_header()
#     show_edit_event_page(event_id)




ui.run()
