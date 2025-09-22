from nicegui import ui

def show_vendor_signin_page():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    with ui.element("div").classes(
    "w-full h-screen flex flex-col md:flex-row m-0 p-0 border rounded-2xl overflow-hidden"
):
    # --- Left Side (Image/Welcome section) ---
        with ui.element("div").classes(
            "relative bg-[url('/assets/skillbridge_signin.png')] bg-cover bg-center h-[40%] md:h-full w-full md:w-1/2 m-0 p-0 flex items-center justify-center"
        ):
            ui.element("div").classes("absolute inset-0 bg-black/40")
        
                # .on_click(lambda: ui.run_javascript("window.location.href = '/signin'"))

        # --- Right Side (Form section) ---
        with ui.column().classes(
            "relative w-full md:w-1/2 h-[60%] md:h-full bg-gray-50 m-0 p-0 flex items-center justify-center px-4 md:px-20"
        ):
            ui.label("Welcome to SkillBridge").classes(
                "text-2xl md:text-3xl font-bold text-center text-black"
            )
            ui.label("Sign in to your account").classes("text-sm md:text-base text-center")

            # Form container
            with ui.element("div").classes("w-full flex flex-col px-1"):
                # Email
                ui.input(placeholder="Email") \
                    .props("flat dense borderless") \
                    .classes("rounded-sm w-full text-base bg-white my-4 px-2")

                # Password
                ui.input(placeholder="Password", password=True, password_toggle_button=True) \
                    .props("flat dense borderless") \
                    .classes("rounded-sm w-full text-base bg-white my-4 px-2")

                with ui.row().classes("w-full justify-end"):
                    ui.link("Forget password?").classes("no-underline text-sm text-primary")

                # Buttons
                ui.button("Login as Company") \
                    .props("no-caps flat") \
                    .classes("text-white text-base bg-primary mt-5 text-center w-full")

                ui.button("Login as User") \
                    .props("no-caps flat") \
                    .classes("text-black bg-gray-200 text-base my-5 text-center w-full")

                # Sign up link
                with ui.row().classes("items-center justify-center space-x-1 gap-0 m-0 p-0"):
                    ui.label("Don't have an account?")
                    ui.link("Sign up", "/vendor_signup").classes("no-underline text-primary")

                

            #     # "or" label
            #     ui.label("or").classes("text-xs text-gray-500 my-1 self-center")

            #     # Signup with Google button
            #     with ui.button().props("flat dense no-caps outlined").classes("bg-white text-black min-w-[300px] border-2 border-black rounded-md flex items-center justify-center space-x-2 self-center"):
            # # Google logo (SVG)
            #         ui.html("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" class="w-5 h-5">
            #             <path fill="#4285F4" d="M24 9.5c3.5 0 6.2 1.5 7.6 2.8l5.5-5.5C33.4 3.8 28.9 2 24 2 14.8 2 7.2 7.8 4 16.2l6.7 5.2C12.4 14.5 17.7 9.5 24 9.5z"/>
            #             <path fill="#34A853" d="M46.1 24.5c0-1.6-.1-2.7-.4-3.9H24v7.4h12.6c-.3 2.1-1.8 5.2-5 7.3l7.6 5.9c4.6-4.3 7.2-10.6 7.2-16.7z"/>
            #             <path fill="#FBBC05" d="M10.7 28.3c-.5-1.5-.8-3.2-.8-5s.3-3.5.8-5L4 13c-1.2 2.4-2 5.2-2 8.3s.7 5.9 2 8.3l6.7-5.3z"/>
            #             <path fill="#EA4335" d="M24 46c6.5 0 11.9-2.1 15.8-5.7l-7.6-5.9c-2 1.4-4.7 2.4-8.2 2.4-6.3 0-11.6-4.2-13.5-10.1l-6.7 5.2C7.2 40.2 14.8 46 24 46z"/>
            #         </svg>""").classes("mr-2")
            #         ui.label("Signup with Google").classes("text-sm font-medium")




ui.run()