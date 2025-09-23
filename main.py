from nicegui import ui,app
from components.header2 import show_header
from pages.home import show_home_page
from pages.add_event import show_add_event_page
from pages.edit_event import show_edit_event_page
from pages.view_event import show_view_event_page
from pages.vendor_page import vendor_dashboard_page
from pages.vendor_signup import show_vendor_signup_page
from pages.vendor_signin import show_vendor_signin_page


ui.add_head_html('''
<style>
.floating-blink-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    animation: blink 1.5s infinite;
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    font-size: 1rem;
    font-weight: bold;
    padding: 14px 24px;
    border-radius: 9999px;
    box-shadow: 0px 4px 15px rgba(37, 99, 235, 0.6);
    transition: transform 0.2s, box-shadow 0.2s;
    z-index: 9999;
}
.floating-blink-button:hover {
    transform: scale(1.08);
    box-shadow: 0px 6px 18px rgba(37, 99, 235, 0.8);
}
@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}
</style>
''')

# Add the CSS for the blinking effect at the very top
ui.add_head_html('''
    <style>
    @keyframes blink {
      0%, 100% { background-color: #f97316 !important; } /* Orange 500 */
      50% { background-color: transparent !important; }
    }
    .blinking-button {
      animation: blink 2s infinite !important;
    }
    </style>
''')

# animation
ui.add_head_html("""
<style>
@keyframes typing-loop {
  0% { width: 0; }
  40% { width: 100%; }
  90% { width: 100%; }
  100% { width: 0; }
}

.typewriter {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  width: 0;
  animation: typing-loop 7s steps(12, end) infinite;
}
</style>
""")


@ui.page("/")
def home_page():
    show_header()
    show_home_page()
    

@ui.page("/add_event")
def add_event_page():
    show_header()
    show_add_event_page()

@ui.page("/edit_event")
def edit_event_page():
    show_header()
    show_edit_event_page()

@ui.page("/view_event")
def view_event_page(id=""):
    show_view_event_page(id)

@ui.page("/edit_event/{job_id}")
def edit_event_page(job_id: int):
    show_header()
    show_edit_event_page(job_id)

@ui.page('/vendor')
def vendor_page():
    vendor_dashboard_page()

@ui.page("/vendor_signup")
def vendor_signup():
    show_vendor_signup_page()

@ui.page("/vendor_signin")
def vendor_signin():
    show_vendor_signin_page()


ui.run()
