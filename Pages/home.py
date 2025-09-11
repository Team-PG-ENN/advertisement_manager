from nicegui import ui
from components.header import show_header
from components.footer import show_footer

# Mock adverts data
adverts = [
    {"id": 1, "title": "Graduate: Ama K.", "desc": "Frontend Developer", "category": "Portfolio"},
    {"id": 2, "title": "Graduate: Kojo M.", "desc": "Data Analyst", "category": "Portfolio"},
    {"id": 3, "title": "Graduate: Rasmiya Hamid.", "desc": "CyberSecurity", "category": "Portfolio"},
    {"id": 4, "title": "Graduate: Frank Asante.", "desc": "Cloud Computing", "category": "Portfolio"}
]

def show_home_page():
    with ui.column().classes('w-screen h-screen p-8'):
        ui.label("Discover Tech Talents in Ghana").classes(
            'text-3xl font-bold text-center mb-6 text-orange-600'
        )
        ui.input('Search adverts...').props('outlined').classes('rounded-full w-1/2 mx-auto')

        with ui.grid(columns=3).classes('gap-6 mt-6'):
            for advert in adverts:
                with ui.card().classes('p-4 shadow-sm'):
                    ui.label(advert["title"]).classes('font-bold text-lg')
                    ui.label(advert["desc"])
                    ui.label(f'Category: {advert["category"]}')

                    ui.button(
                        'View',
                        on_click=lambda e, a=advert: ui.navigate.to(f'/view_event{a["id"]}')
                    ).props("flat dense").classes('bg-orange-500 text-white mt-2')

                    # Edit/Delete only for vendor (later via auth)
                    ui.button(
                        'Edit',
                        on_click=lambda e, a=advert: ui.navigate.to(f'/edit_event{a["id"]}')
                    ).classes('bg-blue-500 text-white mt-2')

                    ui.button(
                        'Delete',
                        on_click=lambda e, a=advert: ui.notify(f'Advert {a["id"]} deleted!')
                    ).classes('bg-red-500 text-white mt-2')



