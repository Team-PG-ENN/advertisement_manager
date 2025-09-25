from nicegui import ui,app
import datetime
from pages.edit_event import show_edit_event_page
import requests
from utils.api import base_url
from functools import partial

# Exposing assets folder
app.add_static_files("/assets","assets")


# {'company': 'Mest Africa', 'verified': True, 'logo': 150&'https://tse4.mm.bing.net/th/id/OIP.pslKeE6ElqR_o2DBg6JaNwAAAA?r=0&cb=ucfimg2&pid=ImgDet&ucfimg=1&w=h=150&c=7&dpr=1.5&o=7&rm=3', 'title': 'Software Development Trainee', 'location': 'Accra, Ghana', 'type': 'Hybrid', 'date_posted': '4 hours ago', 'status': 'Not applied', 'description': 'Mest Africa is hiring recent graduates from their program. They are looking for about 25 web development trainees for a hybrid role.', 'skills': ['Python', 'JavaScript', 'Django'], 'id': 1},
#                 {'company': 'Blossom Academy', 'verified': True, 'logo': 'https://media-exp1.licdn.com/dms/image/C510BAQE6OtVLMbT2jw/company-logo_200_200/0/1519875019395?e=2159024400&v=beta&t=Q2j-EypivTm118lDt88qU_JHaDJRFZ_hlR-D79sZV00', 'title': 'Data Science Fellowship', 'location': 'Kumasi, Ghana', 'type': 'On-site', 'date_posted': 'Yesterday', 'status': 'Not applied', 'description': 'A 6-month fellowship focused on practical data science projects and mentorship. Work with real-world datasets.', 'skills': ['Data Analysis', 'Machine Learning', 'SQL'], 'id': 2},
#                 {'company': 'Soronko Academy', 'verified': True, 'logo': 'https://soronkoacademy.org/wp-content/uploads/2021/05/logo-color-1.png', 'title': 'Web Development Bootcamp', 'location': 'Accra, Ghana', 'type': 'Remote', 'date_posted': '3 days ago', 'status': 'Applied', 'description': 'Intensive bootcamp to become a full-stack web developer. Focus on MERN stack and agile methodologies.', 'skills': ['React', 'Node.js', 'MongoDB'], 'id': 3},
#                 {'company': 'Azubi Africa', 'verified': True, 'logo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6-o3F9t3p3g_9f_1-Q2wJ-4-f_5k-5u5i-g&s', 'title': 'Digital Marketing Specialist', 'location': 'Takoradi, Ghana', 'type': 'Hybrid', 'date_posted': '2025-09-05', 'status': 'Not applied', 'description': 'Join our team to manage digital campaigns and SEO strategies. Gain hands-on experience in a fast-paced environment.', 'skills': ['SEO', 'SEM', 'Social Media Marketing'], 'id': 4},
#                 {'company': 'TechCorp Solutions', 'verified': False, 'logo': 'https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg', 'title': 'UX/UI Design Intern', 'location': 'Remote', 'type': 'Remote', 'date_posted': '2025-09-04', 'status': 'Not applied', 'description': 'Trainee role in user experience and interface design. Learn industry-standard tools and design principles.', 'skills': ['Figma', 'Sketch', 'User Research'], 'id': 5},
#                 {'company': 'DataHub Ghana', 'verified': True, 'logo': 'https://upload.wikimedia.org/wikipedia/commons/d/d9/Node.js_logo.svg', 'title': 'Junior Cybersecurity Analyst', 'location': 'Accra, Ghana', 'type': 'Full-time', 'date_posted': '2025-09-03', 'status': 'Applied', 'description': 'Entry-level position in network security and threat analysis. Opportunity to work with certified professionals.', 'skills': ['Network Security', 'Threat Analysis', 'Cyber Forensics'], 'id': 6},


TECH_CATEGORIES = [
    'All Categories',
    'Web Development',
    'Data Science',
    'Cybersecurity',
    'Digital Marketing',
    'Graphic Design',
    'Mobile Development',
    'Cloud Computing',
    'AI/Machine Learning'
]


def show_home_page():
    response = requests.get(f"{base_url}/view_job")
    json_data = response.json()

    # Main Layout 
    ui.query('.q-page-container').classes('m-0 p-0 gap-0')
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    with ui.column().classes('w-full h-screen items-center'):

       # Hero Section in Grid 
        with ui.row().classes(
            'w-full h-full items-center bg-gray-100 px-10'
        ):
            with ui.element('div').classes(
                'grid grid-cols-1 md:grid-cols-2 gap-8 w-full items-center'
            ):

                # --- Left Column (Text, Search, Tabs) ---
                with ui.column().classes('space-y-4 text-center md:text-left'):
                    ui.label("Discover the World’s Top Tech Talents").classes(
                        'text-2xl md:text-5xl font-extrabold leading-tight text-gray-800'
                    )
                    ui.label(
                        "Explore opportunities with the most skilled tech professionals and discover job openings tailored to your next big project."
                    ).classes('text-gray-600 text-sm md:text-lg')

                    # Tabs
                    with ui.row().classes('mt-6 gap-2 flex-wrap justify-center md:justify-start'):
                        ui.button('All jobs', icon='work').classes(
                            'rounded-full text-white px-4 md:px-6 py-2 text-sm md:text-base'
                        )
                        ui.button('Recent Jobs', icon='business_center').classes(
                            'rounded-full  text-white px-4 md:px-6 py-2 text-sm md:text-base'
                        )
                        ui.button('Companies', icon='domain').classes(
                            'rounded-full bg-gray-200 text-gray-700 px-4 md:px-6 py-2 text-sm md:text-base'
                        )

                    # Search bar
                    with ui.row().classes('w-full items-center mt-4 gap-2 flex-wrap'):
                        ui.input(
                            placeholder='Search for jobs...'
                        ).classes('flex-grow min-w-[180px]').props('rounded outlined')
                        ui.button(icon='search').classes('text-white rounded-full p-3')

                    # Popular searches
                    with ui.row().classes('w-full items-center mt-2 flex-wrap gap-2 justify-center md:justify-start'):
                        ui.label('Popular:').classes('text-gray-500 text-sm font-semibold')
                        for term in ['Web Development', 'UI/UX', 'Data Analytics', 'Digital Marketing']:
                            ui.label(term).classes(
                                'text-sm text-gray-700 font-medium px-2 py-1 bg-gray-100 rounded-full cursor-pointer hover:bg-gray-200'
                            )

                                # --- Right Column (Video) ---
                with ui.card().classes(
                    'w-full aspect-video items-center shadow-lg rounded-2xl overflow-hidden relative'
                ):
                    ui.html('''
                        <video autoplay loop muted playsinline controls class="w-full h-full object-contain rounded-2xl">
                            <source src="./assets/hero-video.mp4">
                            Your browser does not support the video tag.
                        </video>
                    ''')

 

   # --- Advertisements Section ---
    with ui.element('section').classes('w-full px-10 py-12'):
        with ui.row().classes('w-full flex-wrap gap-8'):
            
            # --- Left Column: Advertisements ---
            with ui.column().classes('md:w-full space-y-4'):
                # Category buttons above adverts
                with ui.row().classes('w-full gap-2 items-center justify-center flex flex-wrap'):
                    ui.button('All').props('no-caps').classes("rounded-full bg-pink-500 text-white px-4 py-2")
                    for cat in ['Web Development', 'Data Analytics', 'Digital Marketing','Cloud Computing']:
                        ui.button(cat).props('no-caps flat').classes(
                            "rounded-full bg-gray-200 text-black px-4 py-2 hover:bg-gray-300"
                        )
            with ui.row().classes('w-full md:justify-between'):
                # --- Left Column: Adverts list ---
                with ui.column().classes('w-full md:w-3/5'):
                    advertisements = json_data["adverts"]

                    def view_details(job_id):
                        ui.navigate.to(f'/view_event?id={job_id}')

                    for ad in advertisements:
                        with ui.card().classes(
                            'w-full my-2 p-4 shadow-md rounded-lg border-l-4 border-orange-400 '
                            'hover:bg-gray-50 transition-colors duration-200 cursor-pointer flex-row items-center'
                        ):
                            # Company Logo
                            ui.image(ad['image']).classes(
                                'w-12 h-12 rounded-full border border-gray-300 object-contain flex-shrink-0'
                            )

                            # Job Details
                            with ui.column().classes('flex-grow px-4'):
                                with ui.row().classes('items-center gap-2'):
                                    ui.label(ad['job_title']).classes('text-lg font-bold')
                                
                                ui.label(ad['category']).classes('font-semibold')
                                ui.label(f'• {ad["created_at"]}').classes('text-xs text-gray-500')
                                ui.label(ad['job_description']).classes('text-sm text-gray-700 mt-1')

                                with ui.row().classes('mt-2 flex-wrap gap-1'):
                                    for skill in ad['skills']:
                                        ui.badge(skill).classes(
                                            'bg-gray-200 text-gray-800 text-xs px-2 py-1 rounded-full'
                                        )

                            # Action Buttons
                            with ui.column().classes('flex-shrink-0 items-center gap-2'):
                                ui.icon('bookmark_border').classes('text-gray-500 text-xl cursor-pointer')
                                ui.button(
                                    'View',
                                    on_click=lambda id=ad['_id']: view_details(id)
                                ).classes(
                                    'bg-orange-500 hover:bg-orange-600 text-white font-bold px-4 py-2 rounded'
                                )

                # --- Right Column: Filters Sidebar ---
                with ui.column().classes(
                    'w-full md:w-1/3 bg-gray-50 rounded-lg shadow-sm px-4'
                ):
                    ui.label('Filter Jobs').classes('text-xl font-bold text-gray-800')
                    
                    ui.input(placeholder='Search jobs...').props('outlined').classes('w-full')
                    ui.select(
                        ['Web Development', 'Data Analytics', 'Digital Marketing', 'Graphic Design', 'Cybersecurity'],
                        label='Category'
                    ).classes('w-full')
                    ui.select(
                        ['Mest Africa', 'Blossom Academy', 'Soronko Academy', 'Azubi Africa'],
                        label='Company'
                    ).classes('w-full')
                    ui.select(
                        ['Hybrid', 'On-site', 'Remote', 'Full-time'],
                        label='Job Type'
                    ).classes('w-full')
                    ui.select(
                        ['Accra, Ghana', 'Kumasi, Ghana', 'Takoradi, Ghana', 'Remote'],
                        label='Location'
                    ).classes('w-full')
                    ui.checkbox('Verified Partners Only')
                    ui.button('Apply Filters').props('no-caps flat').classes(
                        'w-full bg-orange-400 hover:bg-orange-600 text-white font-bold rounded'
                    )


  
    # Why Join Section
    with ui.row().classes('w-full justify-center'):
        with ui.element("div").classes('bg-gray-100 rounded-2xl shadow-lg p-8 text-center w-full'):
            ui.label("Why Join SkillBridge?").classes('text-2xl font-bold text-gray-800 py-2')
            ui.label("Connect with digital talent worldwide and find the perfect match for your projects.").classes('text-base text-gray-600 mb-10')
            
            with ui.row().classes('flex flex-row md:w-full md:flex-row flex-wrap text-left justify-center md:gap-10'):
                # Reason 1: Company
                with ui.card().classes(
                    'bg-white rounded-2xl p-6 flex flex-col shadow-md md:w-[47%]'
                ):
                    ui.label("For Companies").classes('text-xl text-primary font-bold')
                    ui.label(
                        "• Access a diverse pool of vetted tech talent from leading training institutions."
                    ).classes('text-base text-gray-600')
                    ui.label(
                        "• Streamline your hiring process with our easy-to-use job posting and management tools."
                    ).classes('text-base text-gray-600')
                    ui.label(
                        "• Partner with top tech education to shape the future workforce."
                    ).classes('text-base text-gray-600')

                # Reason 2: Individuals
                with ui.card().classes(
                    'bg-white flex flex-col rounded-2xl p-6 shadow-md md:w-[47%]'
                ):
                    ui.label("For Individuals").classes('text-xl text-orange-400 font-bold')
                    ui.label(
                        "• Discover exclusive job opportunities from companies that value your training"
                    ).classes('text-base text-gray-600')
                    ui.label(
                        "• Access career resources, interview tips, and hiring materials to boost your profile"
                    ).classes('text-base text-gray-600')
                    ui.label(
                        "• Connect with a community of peers and mentors in the tech industry"
                    ).classes('text-base text-gray-600')

    # Career Resources
    with ui.row().classes('w-full justify-center'):
        with ui.element("div").classes('bg-white shadow-lg p-8 text-center w-full'):
            ui.label("Career Resources").classes('text-2xl font-bold text-gray-800 py-2')
            ui.label("Tips and guides to help you land your dream job.").classes('text-base text-gray-600 md:mb-10')
            
            with ui.row().classes('flex md:w-full md:flex-row flex-wrap justify-center md:gap-8'):
                # Interview tips
                with ui.card().classes(
                    'bg-white rounded-2xl p-6 flex flex-col items-center justify-center text-center shadow-md md:w-[31%]'
                ):
                    ui.icon('lightbulb_outline', size='3rem').props('color=primary')
                    ui.label("Interview Tips").classes('text-lg text-primary font-bold')
                    ui.label(
                        "Ace your next interview"
                    ).classes('text-base text-gray-600')

                # Learning resources
                with ui.card().classes(
                    'bg-white rounded-2xl p-6 flex flex-col items-center justify-center text-center shadow-md md:w-[31%]'
                ):
                    ui.icon('school', size='3rem').props('color=primary')
                    ui.label('Learning Resources').classes('text-xl text-primary font-bold')
                    ui.label(
                        "Enhance your tech skills"
                    ).classes('text-base text-gray-600')

                # Find your path
                with ui.card().classes(
                    'bg-white rounded-2xl p-6 flex flex-col items-center justify-center text-center shadow-md md:w-[31%]'
                ):
                    ui.icon('explore', size='3rem').props('color=primary')
                    ui.label("Find Your Path").classes('text-xl text-primary font-bold')
                    ui.label(
                        'Discover your career journey'
                    ).classes('text-base text-gray-600')


    # About Us Section
    with ui.column().classes('w-full bg-gray-100  my-15 items-center'):
        with ui.row().classes(
            'w-full items-center bg-gray-100 px-10'
        ):
            with ui.element('div').classes(
                'grid grid-cols-1 md:grid-cols-2 gap-8 w-full items-center'
            ):

                # Left column for the 'About Us text'
                with ui.column().classes('space-y-4 md:text-left'):
                    ui.label("About Us").classes(
                        'text-2xl md:text-5xl font-extrabold leading-tight text-gray-800'
                    )
                    ui.label(
                        "Skillbridge was founded on the principle that the right skills can transform lives. We are dedicated to bridge the gap" \
                        "between emerging tech talent and the companies that need them."
                    ).classes('text-gray-600 text-sm md:text-lg')
                    ui.button('Learn More').props('no-caps').classes()

                                # --- Right Column (Video) ---
                with ui.card().classes(
                    'w-full aspect-image items-center shadow-lg rounded-2xl overflow-hidden relative my-10'
                ):
                    ui.image('')



    # Success Stories Section
    
    with ui.row().classes('w-full bg-white py-12 mt-12 justify-center items-center'):
        with ui.column().classes('w-full max-w-5xl items-center'):
            ui.label("Success Stories").classes('text-2xl font-bold text-center mb-8')

            # Use ui.html for the structural HTML and CSS
            ui.html('''
                <style>
                /* Base styles for the entire carousel container */
                .story-carousel-container {
                    width: 100%;
                    display: flex;
                    justify-content: center;
                    overflow: hidden;
                }

                /* Styles for each group of stories */
                .story-group {
                    display: none; 
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 2.5rem;
                    transition: opacity 0.5s ease-in-out;
                }
                .story-group.active {
                    display: flex; 
                    opacity: 1;
                }

                /* Styles for individual story containers */
                .story-container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    text-align: center;
                    width: 300px;
                    flex-shrink: 0;
                }

                /* Mobile responsiveness for the story groups */
                @media (max-width: 768px) {
                    .story-group {
                        flex-direction: column; /* Stack stories on mobile */
                        align-items: center;
                        gap: 1.5rem;
                    }
                    .story-container {
                        width: 90%; /* Adjust width for better fit on small screens */
                    }
                }
                
                /* Styles for the image and text elements */
                .story-image {
                    width: 100px;
                    height: 100px;
                    border-radius: 50%;
                    object-fit: fit;
                    margin-bottom: 1rem;
                }
                .story-text {
                    font-style: italic;
                    color: #4B5563;
                    margin-bottom: 0.5rem;
                }
                .story-name {
                    font-weight: bold;
                    margin-bottom: 1rem;
                }

                /* Styles for the navigation dots */
                .dots {
                    display: flex;
                    justify-content: center;
                    gap: 8px;
                }
                .dot {
                    width: 10px;
                    height: 10px;
                    border-radius: 50%;
                    background-color: #D1D5DB;
                    cursor: pointer;
                }
                .dot.active {
                    background-color: #2563EB;
                }
                </style>

                <div class="story-carousel-container">
                    <div id="group-0" class="story-group active">
                        <div class="story-container">
                            <img src="./assets/Peter.jpg" class="story-image">
                            <div class="story-text">"This platform helped me land my dream job at TechCorp!"</div>
                            <div class="story-name">Peter</div>
                        </div>

                        <div class="story-container">
                            <img src="https://tse4.mm.bing.net/th/id/OIP.pslKeE6ElqR_o2DBg6JaNwAAAA?r=0&cb=ucfimg2&pid=ImgDet&ucfimg=1&w=150&h=150&c=7&dpr=1.5&o=7&rm=3" class="story-image">
                            <div class="story-text">"We found internship opportunities for GROW Web Development cohort6 quickly."</div>
                            <div class="story-name">Mest Africa</div>
                        </div>

                        <div class="story-container">
                            <img src="./assets/Naa.jpg" class="story-image">
                            <div class="story-text">"CyberSafe recruited me straight from the portal. Life changing!"</div>
                            <div class="story-name">Naa Fofo</div>
                        </div>
                    </div>

                    <div id="group-1" class="story-group">
                        <div class="story-container">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" class="story-image">
                            <div class="story-text">"Our company discovered amazing junior developers through this platform."</div>
                            <div class="story-name">TechCorp</div>
                        </div>

                        <div class="story-container">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/d/d9/Node.js_logo.svg" class="story-image">
                            <div class="story-text">"We found skilled talent for our internship program quickly."</div>
                            <div class="story-name">DataHub</div>
                        </div>
                    </div>
                </div>

                <div class="dots mt-4">
                    <div class="dot active" onclick="showGroup(0)"></div>
                    <div class="dot" onclick="showGroup(1)"></div>
                </div>
            ''')

            ui.add_body_html('''
                <script>
                const groups = document.querySelectorAll(".story-group");
                const dots = document.querySelectorAll(".dot");
                let currentGroupIndex = 0;

                function showGroup(index) {
                    // Hide all groups and deactivate all dots
                    groups.forEach(group => group.classList.remove("active"));
                    dots.forEach(dot => dot.classList.remove("active"));

                    // Ensure the index is within bounds and wrap around
                    currentGroupIndex = (index + groups.length) % groups.length;

                    // Show the selected group and activate its dot
                    groups[currentGroupIndex].classList.add("active");
                    dots[currentGroupIndex].classList.add("active");
                }

                // Auto-advance the carousel every 5 seconds
                setInterval(() => {
                    showGroup(currentGroupIndex + 1);
                }, 5000);
                </script>
            ''')

    # verified Companies Section
    with ui.row().classes('w-screen bg-gray-100 py-6 justify-center items-center'):
        with ui.column().classes('w-full max-w-6xl items-center'):
            ui.label('Our Verified Partners').classes(
                'text-2xl font-bold text-center mb-6'
            )

            with ui.row().classes('w-full justify-center items-center gap-4 md:gap-8 flex-wrap'):
                company_logos = [
                    "https://tse4.mm.bing.net/th/id/OIP.pslKeE6ElqR_o2DBg6JaNwAAAA?r=0&cb=ucfimg2&pid=ImgDet&ucfimg=1&w=150&h=150&c=7&dpr=1.5&o=7&rm=3",
                    "data:image/png;base64,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",
                    "data:image/png;base64,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",
                    "https://media-exp1.licdn.com/dms/image/C510BAQE6OtVLMbT2jw/company-logo_200_200/0/1519875019395?e=2159024400&v=beta&t=Q2j-EypivTm118lDt88qU_JHaDJRFZ_hlR-D79sZV00",
                    "data:image/png;base64,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"
                ]

                for logo in company_logos:
                    # Increased min-h-20 for more card height, p-4 for internal padding
                    with ui.card().classes('flex items-center justify-center p-4 shadow-sm rounded-lg w-28 min-h-28'):
                        ui.image(logo).classes('object-contain max-w-full h-auto')
    


    # # Footer
    with ui.element("div").classes('bg-gray-800 w-screen text-white p-6 mt-10 text-center'):
        ui.label("© 2025 SkillBridge - Bridging the future with tech skil").classes("tetx-center")
