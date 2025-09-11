from nicegui import ui
import datetime
from pages.edit_event import show_edit_event_page
import requests
from utils.api import base_url



# {'company': 'Mest Africa', 'verified': True, 'logo': 'https://tse4.mm.bing.net/th/id/OIP.pslKeE6ElqR_o2DBg6JaNwAAAA?r=0&cb=ucfimg2&pid=ImgDet&ucfimg=1&w=150&h=150&c=7&dpr=1.5&o=7&rm=3', 'title': 'Software Development Trainee', 'location': 'Accra, Ghana', 'type': 'Hybrid', 'date_posted': '4 hours ago', 'status': 'Not applied', 'description': 'Mest Africa is hiring recent graduates from their program. They are looking for about 25 web development trainees for a hybrid role.', 'skills': ['Python', 'JavaScript', 'Django'], 'id': 1},
#                 {'company': 'Blossom Academy', 'verified': True, 'logo': 'https://media-exp1.licdn.com/dms/image/C510BAQE6OtVLMbT2jw/company-logo_200_200/0/1519875019395?e=2159024400&v=beta&t=Q2j-EypivTm118lDt88qU_JHaDJRFZ_hlR-D79sZV00', 'title': 'Data Science Fellowship', 'location': 'Kumasi, Ghana', 'type': 'On-site', 'date_posted': 'Yesterday', 'status': 'Not applied', 'description': 'A 6-month fellowship focused on practical data science projects and mentorship. Work with real-world datasets.', 'skills': ['Data Analysis', 'Machine Learning', 'SQL'], 'id': 2},
#                 {'company': 'Soronko Academy', 'verified': True, 'logo': 'https://soronkoacademy.org/wp-content/uploads/2021/05/logo-color-1.png', 'title': 'Web Development Bootcamp', 'location': 'Accra, Ghana', 'type': 'Remote', 'date_posted': '3 days ago', 'status': 'Applied', 'description': 'Intensive bootcamp to become a full-stack web developer. Focus on MERN stack and agile methodologies.', 'skills': ['React', 'Node.js', 'MongoDB'], 'id': 3},
#                 {'company': 'Azubi Africa', 'verified': True, 'logo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6-o3F9t3p3g_9f_1-Q2wJ-4-f_5k-5u5i-g&s', 'title': 'Digital Marketing Specialist', 'location': 'Takoradi, Ghana', 'type': 'Hybrid', 'date_posted': '2025-09-05', 'status': 'Not applied', 'description': 'Join our team to manage digital campaigns and SEO strategies. Gain hands-on experience in a fast-paced environment.', 'skills': ['SEO', 'SEM', 'Social Media Marketing'], 'id': 4},
#                 {'company': 'TechCorp Solutions', 'verified': False, 'logo': 'https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg', 'title': 'UX/UI Design Intern', 'location': 'Remote', 'type': 'Remote', 'date_posted': '2025-09-04', 'status': 'Not applied', 'description': 'Trainee role in user experience and interface design. Learn industry-standard tools and design principles.', 'skills': ['Figma', 'Sketch', 'User Research'], 'id': 5},
#                 {'company': 'DataHub Ghana', 'verified': True, 'logo': 'https://upload.wikimedia.org/wikipedia/commons/d/d9/Node.js_logo.svg', 'title': 'Junior Cybersecurity Analyst', 'location': 'Accra, Ghana', 'type': 'Full-time', 'date_posted': '2025-09-03', 'status': 'Applied', 'description': 'Entry-level position in network security and threat analysis. Opportunity to work with certified professionals.', 'skills': ['Network Security', 'Threat Analysis', 'Cyber Forensics'], 'id': 6},
            


def show_home_page():
    response = requests.get(f"{base_url}/view_job")
    for advert in response.json():
        print(advert)
    # --- Hero Section (your existing content) ---
    # Set up the main page with a full-screen layout and some padding.
    with ui.column().classes('w-screen h-screen items-center'):

        # --- Hero Section ---
        # A responsive row to hold the text and the video.
        # It stacks them as a column on small screens (flex-col) and
        # changes to a row on medium screens and up (md:flex-row).
        with ui.row().classes('w-full flex-row items-center justify-between mt-10 px-6 md:px-16 gap-8 max-w-screen-xl mx-auto'):
            
            # --- Left Side: Text and Headings with Search Bar ---
            with ui.column().classes('w-full md:w-1/2 space-y-4 text-center md:text-left'):
                ui.label("Discover the World’s Top Designers").classes(
                    'text-3xl md:text-5xl font-extrabold leading-tight text-gray-800'
                )
                ui.label(
                    "Explore work from the most talented and accomplished designers ready to take on your next project."
                ).classes('text-gray-600 text-base md:text-lg')
                
                # Tabbed navigation
                with ui.row().classes('mt-6 gap-2'):
                    ui.button('Shots', icon='bolt').classes('rounded-full bg-black text-white px-6 py-2')
                    ui.button('Designers', icon='people').classes('rounded-full bg-gray-200 text-gray-800 px-6 py-2')
                    ui.button('Services', icon='handyman').classes('rounded-full bg-gray-200 text-gray-800 px-6 py-2')

                # Search bar
                with ui.row().classes('w-full items-center mt-4'):
                    ui.input(placeholder='What type of design are you interested in?').classes('flex-grow').props('rounded outlined')
                    ui.button(icon='search').classes('bg-pink-500 text-white rounded-full p-3')
                
                # Popular searches
                with ui.row().classes('w-full items-center mt-2'):
                    ui.label('Popular:').classes('text-gray-500 text-sm font-semibold')
                    for term in ['dashboard', 'landing page', 'e-commerce', 'logo']:
                        ui.label(term).classes('text-sm text-gray-700 font-medium px-2 py-1 bg-gray-100 rounded-full cursor-pointer hover:bg-gray-200')


            # # --- Right Side: Image Container ---
            # # A card container for the image, giving it a clean, modern look.
            # with ui.card().classes('w-full md:w-1/2 h-[250px] md:h-[400px] shadow-lg rounded-2xl overflow-hidden relative bg-green-900'):
            #     # Embedded HTML with the image.
            #     ui.html('''
            #     <img src="https://placehold.co/600x400/004c00/ffffff?text=Illustration+Placeholder" 
            #          class="w-full h-full object-cover">
            #     ''')
    


# --- Advertisements Section ---
    with ui.row().classes('w-full mt-12 px-4 md:px-12 lg:px-24 flex-wrap justify-center'):
        # Main container for the job ads list
        with ui.column().classes('w-full lg:w-3/5 xl:w-1/2'):
            ui.label('Latest Job Opportunities').classes('text-2xl font-bold text-gray-800 mb-6')
            
            # A list of advertisement data
            advertisements = []

            # Function to handle button clicks and navigate
            def view_details(job_id):
                ui.navigate.to('/view_event/')

            # Loop to create each job advertisement card
            for ad in advertisements:
                with ui.card().classes('w-full my-2 p-2 shadow-md rounded-lg border-l-4 border-orange-500 hover:bg-gray-50 transition-colors duration-200 cursor-pointer flex-row items-center'):
                    # Company Logo
                    ui.image(ad['logo']).classes('w-12 h-12 rounded-full border border-gray-300 object-contain flex-shrink-0')
                    
                    # Middle section with job details
                    with ui.column().classes('flex-grow px-4'):
                        with ui.row().classes('items-center gap-2'):
                            ui.label(ad['title']).classes('text-lg font-bold')
                            if ad['verified']:
                                ui.tooltip('Verified Partner')
                                ui.icon('verified').classes('text-blue-500 text-sm')
                                ui.label('Verified').classes('text-blue-500 text-sm')
                        
                        # Tightly packed company, location, and date
                        with ui.row().classes('items-center text-sm text-gray-600 space-x-1'):
                            ui.label(ad['company']).classes('font-semibold')
                            ui.label(f'• {ad["location"]}')
                            ui.label(f'• {ad["type"]}')
                            ui.label(f'• {ad["date_posted"]}').classes('text-xs text-gray-500')
                        
                        ui.label(ad['description']).classes('text-sm text-gray-700 mt-1')

                        # Skills list
                        with ui.row().classes('mt-2 flex-wrap gap-1'):
                            for skill in ad['skills']:
                                ui.badge(skill).classes('bg-gray-200 text-gray-800 text-xs px-2 py-1 rounded-full')
                        
                    # View Details button to the right, with bookmark icon
                    with ui.column().classes('flex-shrink-0 items-center gap-2'):
                        ui.icon('bookmark_border').classes('text-gray-500 text-xl cursor-pointer')
                        ui.button('View', on_click=lambda id=ad['id']: view_details(id)).classes('bg-orange-500 hover:bg-orange-600 text-white font-bold')

        # Filter and search sidebar
        with ui.column().classes('w-full lg:w-1/3 xl:w-1/4 mt-6 lg:mt-0 p-4 bg-gray-50 rounded-lg shadow-sm'):
            ui.label('Filter Jobs').classes('text-xl font-bold text-gray-800 mb-4')
            
            ui.input(placeholder='Search jobs...').props('outlined').classes('w-full mb-4')
            
            ui.select(
                ['Web Development', 'Data Analytics', 'Digital Marketing', 'Graphic Design', 'Cybersecurity'],
                label='Category'
            ).classes('w-full mb-4')

            ui.select(
                ['Mest Africa', 'Blossom Academy', 'Soronko Academy', 'Azubi Africa'],
                label='Company'
            ).classes('w-full mb-4')

            ui.select(
                ['Hybrid', 'On-site', 'Remote', 'Full-time'],
                label='Job Type'
            ).classes('w-full mb-4')

            ui.select(
                ['Accra, Ghana', 'Kumasi, Ghana', 'Takoradi, Ghana', 'Remote'],
                label='Location'
            ).classes('w-full mb-4')

            ui.checkbox('Verified Partners Only').classes('mb-4')

            ui.button('Apply Filters').classes('w-full bg-orange-500 hover:bg-blue-600 text-white')



    # Why Join Section
    with ui.element("div").classes('bg-blue-100 mt-10 p-8 text-center'):
        ui.label("Why Join SkillBridge?").classes('text-2xl font-bold mb-2')
        ui.label("Advertise your job roles and connect with digital talent worldwide.").classes('text-gray-600')

    # Companies Section
    with ui.row().classes('w-screen bg-gray-100 py-6 mt-12 justify-center items-center'):
        with ui.column().classes('w-full max-w-6xl items-center'):
            ui.label("Our Verified Partners").classes(
                'text-2xl font-bold text-center mb-6'
            )

            with ui.row().classes('w-full justify-center items-center gap-4 md:gap-8 flex-wrap'):
                company_logos = [
                    "https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg",
                    "https://upload.wikimedia.org/wikipedia/commons/1/1f/Python_logo_01.svg",
                    "https://upload.wikimedia.org/wikipedia/commons/d/d9/Node.js_logo.svg",
                    "https://upload.wikimedia.org/wikipedia/commons/4/4f/Cib-digitalocean.svg",
                    "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg"
                ]

                for logo in company_logos:
                    # Increased min-h-20 for more card height, p-4 for internal padding
                    with ui.card().classes('flex items-center justify-center p-4 shadow-sm rounded-lg w-28 min-h-20'):
                        # Added max-w-full and h-auto to the image for better fitting and responsiveness
                        ui.image(logo).classes('object-contain max-w-full h-auto')




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
                    display: none; /* Hidden by default */
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 2.5rem;
                    transition: opacity 0.5s ease-in-out;
                }
                .story-group.active {
                    display: flex; /* Show the active group */
                    opacity: 1;
                }

                /* Styles for individual story containers */
                .story-container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    text-align: center;
                    width: 280px;
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
                    object-fit: cover;
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
                            <img src="https://randomuser.me/api/portraits/women/44.jpg" class="story-image">
                            <div class="story-text">"This platform helped me land my dream job at TechCorp!"</div>
                            <div class="story-name">Alice Johnson</div>
                        </div>

                        <div class="story-container">
                            <img src="https://randomuser.me/api/portraits/men/32.jpg" class="story-image">
                            <div class="story-text">"I transitioned into Data Analytics with ease thanks to the opportunities posted here."</div>
                            <div class="story-name">Bob Smith</div>
                        </div>

                        <div class="story-container">
                            <img src="https://randomuser.me/api/portraits/women/68.jpg" class="story-image">
                            <div class="story-text">"CyberSafe recruited me straight from the portal. Life changing!"</div>
                            <div class="story-name">Clara Evans</div>
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


    


    # # Footer
    with ui.element("div").classes('bg-gray-800 w-screen text-white p-6 mt-10 text-center'):
        ui.label("© 2025 SkillBridge - Bridging the future with tech skil").classes("tetx-center")