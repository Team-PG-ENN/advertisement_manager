# add_event.py
from nicegui import ui
import requests 
from utils.api import base_url

def save_event(data):
    response = requests.post(f"{base_url}/add_advert", data)
    print(response.json())


# global in-memory event store (can be moved to a database later)
events = []
event_id_counter = 1


def add_event(title, desc, category, price):
    """Add new event to storage"""
    global event_id_counter
    events.append({
        "id": event_id_counter,
        "title": title,
        "desc": desc,
        "category": category,
        "price": price,
    })
    event_id_counter += 1
    ui.notify("✅ Event added successfully!")


def show_add_event_page():
    ui.label("➕ Add New Event").classes(
        "text-3xl font-bold text-orange-600 mb-6 text-center"
    )

    # Input fields
    title_input = ui.input("Event Title").props("outlined").classes("w-full mb-3")
    desc_input = ui.textarea("Event Description").props("outlined").classes("w-full mb-3")
    
    category_input = ui.select(
        ["IT", "Business", "Design", "Data", "Other"], 
        label="Category"
    ).props("outlined").classes("w-full mb-3")

    price_input = ui.input("Price").props("outlined type=number").classes("w-full mb-3")


    # Save button
    def save_event():
        if not title_input.value or not desc_input.value:
            ui.notify("⚠️ Please fill in all required fields", color="red")
            return
        add_event(title_input.value, desc_input.value, category_input.value, price_input.value)
        # reset inputs
        title_input.value, desc_input.value, category_input.value, price_input.value = "", "", "", ""

    ui.button("Save Event", on_click=lambda:save_event({
        "title":title_input.value,
        "descs":desc_input.value,
        "category":category_input.value,
        "price":price_input.value


    })).classes(
        "bg-orange-600 text-white px-6 py-2 rounded-lg hover:bg-orange-700"
    )
