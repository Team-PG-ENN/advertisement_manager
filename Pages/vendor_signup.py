from nicegui import ui


def show_vendor_signup_page():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    with ui.element("div").classes(
    "w-full h-screen flex flex-col md:flex-row m-0 p-0 border rounded-2xl overflow-hidden"
):
    # --- Left Side (Image/Welcome section) ---
        with ui.element("div").classes(
            "relative bg-[url('/assets/signup.png')] bg-cover bg-center h-[40%] md:h-full w-full md:w-1/2 m-0 p-0 flex items-center justify-center"
        ):
            ui.element("div").classes("absolute inset-0 bg-black/40")
        
                # .on_click(lambda: ui.run_javascript("window.location.href = '/signin'"))

        # --- Right Side (Form section) ---
        with ui.column().classes(
            "relative w-full md:w-1/2 h-[60%] md:h-full bg-gray-50 m-0 p-0 flex items-center justify-center px-4 md:px-20"
        ):
            ui.label("Create your account").classes(
                "text-2xl md:text-3xl font-bold text-center text-black"
            )
            with ui.row().classes("items-center justify-center text-base space-x-1 gap-0 m-0 p-0"):
                    ui.label("Already have an account?")
                    ui.link("Log in", "/vendor_signin").classes("no-underline text-primary")

            # Form container
            with ui.element("div").classes("w-full flex flex-col px-1"):
                # Email
                ui.input(placeholder="Email address") \
                    .props("flat dense borderless") \
                    .classes("rounded-sm w-full text-base bg-white my-4 px-2")

                # Password
                ui.input(placeholder="Password", password=True, password_toggle_button=True) \
                    .props("flat dense borderless") \
                    .classes("rounded-sm w-full text-base bg-white my-4 px-2")
                
                 # Password confirmation
                ui.input(placeholder="Confirm Password", password=True, password_toggle_button=True) \
                    .props("flat dense borderless") \
                    .classes("rounded-sm w-full text-base bg-white my-4 px-2")

                with ui.row().classes("w-full justify-center"):
                    ui.radio(['User', 'Company'], value='User').props('inline')

                # Buttons
                ui.button("Sign up") \
                    .props("no-caps flat") \
                    .classes("text-white text-base bg-primary my-5 text-center w-full")


                # Sign up link
                with ui.row().classes("items-center justify-center space-x-2 gap-0 m-0 p-0"):
                    ui.label("By creating an account, you agree to SkillBridge's")
                    ui.link("Terms of Service", "/terms_of_service").classes("no-underline text-primary")
                    ui.label('and')
                    ui.link("Privacy Policy", "/terms_of_service").classes("no-underline text-primary")




ui.run()