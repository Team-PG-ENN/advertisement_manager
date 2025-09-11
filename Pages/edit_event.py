# edit_event.py
from nicegui import ui
from pages.add_event import events


def update_event(event_id, title, desc, category, price):
    """Update an existing event by ID"""
    for event in events:
        if event["id"] == event_id:
            event["title"] = title
            event["desc"] = desc
            event["category"] = category
            event["price"] = price
            ui.notify(f"✅ Event ID {event_id} updated successfully!")
            break


# @ui.page("/edit/{event_id}")
def show_edit_event_page(event_id: int):
    """Edit event page"""
    # Find the event by ID
    event = next((e for e in events if e["id"] == event_id), None)
    if not event:
        ui.label("⚠️ Event not found").classes("text-red-600 text-xl")
        return

    ui.label("✏️ Edit Event").classes(
        "text-3xl font-bold text-blue-600 mb-6 text-center"
    )

    # Pre-filled inputs
    title_input = ui.input("Event Title", value=event["title"]).props("outlined").classes("w-full mb-3")
    desc_input = ui.textarea("Event Description", value=event["desc"]).props("outlined").classes("w-full mb-3")
    category_input = ui.input("Category", value=event["category"]).props("outlined").classes("w-full mb-3")
    price_input = ui.input("Price", value=event["price"]).props("outlined type=number").classes("w-full mb-3")

    # Save changes
    def save_changes():
        if not title_input.value or not desc_input.value:
            ui.notify("⚠️ Please fill in all required fields", color="red")
            return
        update_event(
            event_id,
            title_input.value,
            desc_input.value,
            category_input.value,
            price_input.value,
        )

    ui.button("💾 Update Event", on_click=save_changes).classes(
        "bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700"
    )


ui.run()