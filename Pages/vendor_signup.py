from nicegui import ui, run
import requests
from utils.api import base_url


_signup_btn: ui.button = None


def _run_signup(data):
    return requests.post(f"{base_url}/vendors/register", data=data)


async def _signup(data):
    _signup_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_signup, data)
    print(response.status_code, response.content)
    _signup_btn.props(remove="disable loading")
    if response.status_code == 200:
        return ui.navigate.to("/vendor/signin")
    elif response.status_code == 409:
        return ui.notify(message="User already exits!", type="warning")


def show_vendor_signup_page():
    global _signup_btn
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    with ui.element("div").classes(
        "w-full h-screen flex flex-col md:flex-row m-0 p-0 border rounded-2xl overflow-hidden"
    ):
        # --- Left Side (Image/Welcome section) ---
        with ui.element("div").classes(
            "relative bg-[url('/assets/signupimage.png')] bg-cover bg-center h-[40%] md:h-full w-full md:w-1/2 m-0 p-0 flex items-center justify-center"
        ):
            ui.element("div").classes("absolute inset-0 bg-black/40")

            # google fonts
            ui.add_head_html(
                """
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Lobster&family=Poppins:wght@100&display=swap" rel="stylesheet">
            <style>
                    .font-poppins{font-family:'Poppins', sans-serif;}
                    .font-roboto {font-family; 'Roboto', sans-serif;}
                    .font-lobster {font-family: 'Lobster', cursive;}
                    .font {font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif}
            </style>              
            """
            )

            # Container for typewriter text
            ui.add_head_html(
                """
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
                """
            )

            with ui.element("div").classes(
                "relative z-10 flex flex-col items-center justify-center font-lobster text-primary"
            ):
                ui.label("Welcome to SkillBridge").classes(
                    "text-3xl md:text-4xl font-bold text-center typewriter"
                )

                # .on_click(lambda: ui.run_javascript("window.location.href = '/signin'"))

        # --- Right Side (Form section) ---
        with ui.column().classes(
            "relative w-full md:w-1/2 h-[60%] md:h-full bg-gray-50 m-0 p-0 flex items-center justify-center px-4 md:px-20"
        ):
            ui.label("Create your account").classes(
                "text-2xl md:text-3xl font-bold text-center text-black"
            )
            with ui.row().classes(
                "items-center justify-center text-base space-x-1 gap-0 m-0 p-0"
            ):
                ui.label("Already have an account?")
                ui.link("Log in", "/vendor_signin").classes("no-underline text-primary")

            # Form container
            with ui.element("div").classes("w-full flex flex-col px-1"):
                # Vendor
                vendor_name = (
                    ui.input(placeholder="Vendor")
                    .props("flat dense borderless")
                    .classes("rounded-sm w-full text-base bg-white my-4 px-2")
                )

                # Email
                email = (
                    ui.input(placeholder="Email address")
                    .props("flat dense borderless")
                    .classes("rounded-sm w-full text-base bg-white my-4 px-2")
                )

                # Password
                password = (
                    ui.input(
                        placeholder="Password",
                        password=True,
                        password_toggle_button=True,
                    )
                    .props("flat dense borderless")
                    .classes("rounded-sm w-full text-base bg-white my-4 px-2")
                )

                # Password confirmation
                #    ui.input(placeholder="Confirm Password", password=True, password_toggle_button=True) \
                #         .props("flat dense borderless") \
                #         .classes("rounded-sm w-full text-base bg-white my-4 px-2")

                with ui.row().classes("w-full justify-center"):
                    ui.radio(["User", "Company"], value="User").props("inline")

                # Buttons
                _signup_btn = (
                    ui.button(
                        "Sign up",
                        on_click=lambda: _signup(
                            {
                                "vendor_name": vendor_name.value,
                                "email": email.value,
                                "password": password.value,
                            }
                        ),
                    )
                    .props("no-caps flat")
                    .classes("text-white text-base bg-primary my-5 text-center w-full")
                )

                # Sign up link
                with ui.row().classes(
                    "items-center justify-center space-x-2 gap-0 m-0 p-0"
                ):
                    ui.label("By creating an account, you agree to SkillBridge's")
                    ui.link("Terms of Service", "/terms_of_service").classes(
                        "no-underline text-primary"
                    )
                    ui.label("and")
                    ui.link("Privacy Policy", "/terms_of_service").classes(
                        "no-underline text-primary"
                    )


ui.run()
