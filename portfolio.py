import datetime as dt
import streamlit as st
from streamlit_extras.grid import grid
import json
from functions import (
    image_border_radius,
    image_border_radius_url,
    display_text_in_colored_square,
    create_scrollable_section,
    tech_stack,
    image_carousel
)

st.set_page_config(
    page_title = "Rafael Silva Coelho - Portfolio",
    layout = "wide"
)

#TITLE
st.markdown("<i><h1 style='text-align:center'>Rafael Silva Coelho - PORTFOLIO</h1></i>",
            unsafe_allow_html = True)

#TABS
tabs = st.tabs([
    "$$\\Large{\\textbf{    Introduction    }}$$",
    "$$\\Large{\\textbf{    Portfolio Projects    }}$$",
    "$$\\Large{\\textbf{    Tech Stacks / Skills    }}$$",
    "$$\\Large{\\textbf{    GitHub Projects    }}$$"
])

with tabs[0]:#INTRODUCTION
    st.markdown("<h1 style='text-align:center'>Introduction</h1>",
                unsafe_allow_html = True)
    st.divider()
    grid1 = grid([4, 0.1, 1], vertical_align = True)
    container1 = grid1.container()
    grid1.container()
    container2 = grid1.container()
    #image_border_radius("./assets/rafael001.jpeg", 20, 100, 100, container2)
    with container2:
        local_images = [
            "assets/rafael001.jpeg", 
            "assets/rafael002.jpeg", 
            "assets/rafael003.jpeg",
            "assets/rafael004.jpeg"]
        image_carousel(local_images)
    container1.markdown(f"""<div style='font-size:25px'>
                        &#8226 Bachelor's degree in Mathematics at Federal University of Paraná (UFPR) - Brazil.<br>
                        &#8226 Data Scientist and Machine Learning Engineer with over {str(dt.datetime.now().year - 2020)} years of experience in the industry.<br>
                        &#8226 Highly proficient in Data Science, Machine Learning, 
                        Computer Vision and Cybersecurity.<br>
                        &#8226 Developing and deploying machine learning models to solve real-world problems,
                        such as predictive models, anomaly detection and other models to be applied in industry areas,
                        such as Finance, Marketing, Commodities, Retail etc.<br>
                        &#8226 Recently worked in KPMG, one of the Big Four accounting companies, for over a year.<br><br><br>
            </div>""",
            unsafe_allow_html = True)
    cols = container1.columns(2)
    with cols[0]:
        st.link_button(
            "LinkedIn",
            "https://www.linkedin.com/in/rafaelcoelho1409/",
            type = "primary",
            use_container_width = True
        )
    with cols[1]:
        st.link_button(
            "GitHub",
            "https://github.com/rafaelcoelho1409/",
            type = "primary",
            use_container_width = True
        )
    st.divider()


    #MY AREAS OF EXPERTISE
    main_areas1 = [
        "Data<br>Science",
        "Data<br>Engineering",
        "Data<br>Analytics",
        "Machine<br>Learning",
        "Automation<br>(RPA)",
        "Artificial<br>Intelligence",
        "Anomaly<br>Detection",
        "Computer<br>Vision"
    ]
    main_areas2 = [
        "Open Source Intelligence (OSINT)",
        "Pentesting"
    ]
    st.markdown("<i><h2 style='text-align:center'>My areas of expertise</h2></i>",
                unsafe_allow_html = True)
    st.markdown("<b><h3 style='text-align:center'>Data Science & Artificial Intelligence</h3></b>",
                unsafe_allow_html = True)
    grid3 = grid(len(main_areas1))
    for x in main_areas1:
        display_text_in_colored_square(
            f"<h3>{x}</h3>",
            grid3,
            "gray")
    st.markdown("<b><h3 style='text-align:center'>Cybersecurity</h3></b>",
                unsafe_allow_html = True)
    grid4 = grid(len(main_areas2))
    for x in main_areas2:
        display_text_in_colored_square(
            f"<h3>{x}</h3>",
            grid4,
            "gray")
    st.divider()


with tabs[1]: #PORTFOLIO PROJECTS
    st.markdown("<h1 style='text-align:center'>Portfolio Projects</h1>",
                unsafe_allow_html = True)
    st.divider()
    #--------------------------------------------------------------------
    style1 = grid([1, 0.2, 2])
    image1 = style1.container()
    image_border_radius_url(
        "./assets/coelho_finance_logo.png",
        "https://coelhofinance.streamlit.app/",
        20, 100, 100, image1)
    image1.divider()
    with image1:
        image_carousel([
            f"assets/coelhofinance{x:0>2}.png" for x in range(1, 11)
        ])
    style1.container()
    description1 = style1.container()
    description1.write("$$\\Huge{\\textbf{COELHO Finance}}$$")
    description1.markdown("""<div style='font-size:25px'>
                        Get to know <a href='https://coelhofinance.streamlit.app'>COELHO Finance</a>,
                        a new powerful tool to help you make informed investment decisions, 
                        track your investments and identify opportunities. With COELHO Finance, 
                        you can have the confidence to take control of your finances 
                        and achieve your investment goals.<br><br>
                        This Financial Market platform was developed with the intention of being a 
                        personal portfolio project to test lots of Data Science, Machine Learning
                        and Artificial Intelligence tools and frameworks applied to Financial Market. 
                        For now, the access to the platform is free.</div>""", unsafe_allow_html = True)
    st.divider()
    #--------------------------------------------------------------------
    style2 = grid([1, 0.2, 2])
    image2 = style2.container()
    image_border_radius_url(
        "./assets/f1_home.jpg",
        "https://f1analytics.streamlit.app/",
        20, 100, 100, image2)
    image2.divider()
    with image2:
        image_carousel([
            f"assets/f1analytics{x:0>2}.png" for x in range(1, 11)
        ])
    style2.container()
    description2 = style2.container()
    description2.write("$$\\Huge{\\textbf{Formula 1 Analytics}}$$")
    description2.markdown("""<div style='font-size:25px'>
    Discover the exhilarating world of Formula One racing like never before with 
    <a href='https://f1analytics.streamlit.app/'>Formula One Analytics</a>, your ultimate 
    destination for everything F1. From the rich history and iconic circuits to in-depth analyses 
    of each season, our Overview section immerses you in the sport's storied legacy.<br><br>
    Dive deeper into detailed statistics and patterns in the Insights section, perfect for enthusiasts 
    ager to understand the nuances of track performances and driver strategies. Stay up-to-date with 
    comprehensive reviews of each season in our Seasons section, offering exclusive 
    insights into key race strategies and driver skills.<br><br>
    And don't miss the revolutionary AI Space, where cutting-edge Machine Learning technology meets 
    the thrill of F1, promising to reshape how we experience this fascinating sport. 
    Join us at Formula One Analytics for a unique journey into the heart of Formula 1 racing, 
    where data-driven excitement meets the roar of the engines! 🏎️🏁</div>""", unsafe_allow_html = True)
    st.divider()
    #--------------------------------------------------------------------
    style3 = grid([1, 0.2, 2])
    image3 = style3.container()
    image_border_radius_url(
        "./assets/coelho_vision_logo.png",
        "https://coelhovision.streamlit.app/",
        20, 100, 100, image3)
    image3.divider()
    with image3:
        image_carousel([
            f"assets/coelhovision{x:0>2}.png" for x in range(1, 11)
        ])
    style3.container()
    description3 = style3.container()
    description3.write("$$\\Huge{\\textbf{COELHO VISION}}$$")
    description3.markdown("""<div style='font-size:25px'>
    <b><a href='https://coelhovision.streamlit.app/'>COELHO VISION</a>: Revolutionizing Computer Vision</b><br><br>
    Explore COELHO VISION, a cutting-edge platform utilizing OpenCV, 
    Ultralytics, and MediaPipe for advanced Computer Vision applications. Key offerings include:<br><br>
    <b>1) Object Detection:</b> For object, image classification, and face detection.<br>
    <b>2) Image Segmentation:</b> Precise segmentation for detailed image analysis.<br>
    <b>3) Pose Estimation:</b> Tools for gesture recognition and motion analysis.<br>
    <b>4) Live Camera Integration:</b> Apply these technologies in real-time using your device's camera.<br>
    <br>
    Ideal for developers and tech enthusiasts, COELHO VISION is at the forefront of integrating AI with Computer Vision, providing practical, innovative solutions for digital imagery.
    <br><br>
    <b><i>Discover more with COELHO VISION – where technology meets vision.</i></b></div>""", unsafe_allow_html = True)
    st.divider()
    #--------------------------------------------------------------------
    style4 = grid([1, 0.2, 2])
    image4 = style4.container()
    image_border_radius_url(
        "./assets/pentesting_automation_logo.png",
        "https://github.com/rafaelcoelho1409/PentestingAutomation/",
        20, 100, 100, image4)
    image4.divider()
    with image4:
        image_carousel([
            f"assets/pentestingautomation{x:0>3}.png" for x in range(1, 4)
        ])
    style4.container()
    description4 = style4.container()
    description4.write("$$\\Huge{\\textbf{Pentesting Automation}}$$")
    description4.markdown("""<div style='font-size:25px'>
    <b>Pentesting Automation</b> is a complex pentesting automation which scans
    more than 20 types of web vulnerabilities in an automated way, saving time
    from manual work, allowing to focus on tasks which manual and careful analysis
    is necessary.<br><br>
    This automation was built with KALI Linux VM, and several Go, Bash
    and Python tools.""", unsafe_allow_html = True)
    st.divider()
    #--------------------------------------------------------------------
    style5 = grid([1, 0.2, 2])
    image5 = style5.container()
    image_border_radius_url(
        "./assets/coelho_genai_logo.png",
        "https://github.com/rafaelcoelho1409/COELHOGenAI/",
        20, 100, 100, image5)
    image5.divider()
    with image5:
        image_carousel([
            f"assets/coelhogenai{x:0>3}.png" for x in range(0, 5)
        ])
    style5.container()
    description5 = style5.container()
    description5.write("$$\\Huge{\\textbf{Pentesting Automation}}$$")
    description5.markdown("""<div style='font-size:25px'>
    <b>COELHO GenAI</b> is a platform that connects the user to open source 
    Large Language Models like Llama 3.1 (Meta), Gemma 2 (Google), 
    Phi 3.5 (Microsoft) and Qwen 2.5 through Ollama, allowing users to have 
    their own Language Model interface with privacy using the following tools:<br><br>
    <b>1) Assistant</b><br>
    Assistant is a simple chatbot that can answer the questions you have 
    in order to solve problems, have new thoughts and ideas, build new ideas 
    and so on.<br>
    <b>2) Information Retrieval</b><br>
    Information Retrieval connects user local LLM to online tools, such as DuckDuckGo, 
    Wikipedia, PubMed etc.<br>
    <b>3) Data Science</b><br>
    Data Science tool allows user to use autonomous AI agents to explore and 
    to make data analysis and data science over data the user supplies to LLM.<br>
    <b>4) Prompt Engineering</b><br>
    Prompt Engineering is a test tool that allows users to use over 4000 
    ready prompts coming from LangChain Hub for various tasks.""", unsafe_allow_html = True)
    st.divider()


with tabs[2]: #TECH STACKS / SKILLS
    tech_images = json.load(open("tool_images.json"))
    st.markdown("<h1 style='text-align:center'>Tech Stacks / Skills</h1>",
                unsafe_allow_html = True)
    st.divider()
    tabs_tech_stacks = st.tabs([
        "$$\\Large{\\textbf{    Data Science \& Artificial Intelligence    }}$$",
        "$$\\Large{\\textbf{    Cybersecurity    }}$$",
    ])

    with tabs_tech_stacks[0]: #DATA SCIENCE & ARTIFICIAL INTELLIGENCE
        tech_cols = grid([2, 0.2, 2])
        tech_cols1 = tech_cols.container()
        tech_cols.container()
        tech_cols2 = tech_cols.container()
        tech_cols1.markdown("<h2><u>Artificial Intelligence / Machine Learning</u></h2>", unsafe_allow_html = True)
        grid_ = tech_cols1.columns(6)
        tech_stack(
            grid_,
            ["TensorFlow", "PyTorch", "Keras", "Scikit Learn", "XGBoost", "Neural Prophet"],
            [" ADTK", "Statsmodels", "UMAP"],
            tech_images
        )
        tech_cols1.markdown("<h2><u>Generative AI - Large Language Models (LLMs)</u></h2>", unsafe_allow_html = True)
        grid_ = tech_cols1.columns(6)
        tech_stack(
            grid_,
            ["Hugging Face Transformers", "LangChain", "Ollama"],
            [],
            tech_images
        )
        tech_cols1.markdown("<h2><u>Computer Vision</u></h2>", unsafe_allow_html = True)
        grid_1 = tech_cols1.columns(6)
        tech_stack(
            grid_1,
            ["OpenCV", "Ultralytics", "MediaPipe", "OpenVINO", "RoboFlow"],
            [],
            tech_images
        )
        tech_cols1.markdown("<h2><u>Data Science & Data Engineering</u></h2>", unsafe_allow_html = True)
        grid_2 = tech_cols1.columns(6)
        tech_stack(
            grid_2,
            ["NumPy", "Pandas", "Plotly", "PySpark", "Polars"],
            [],
            tech_images
        )
        tech_cols1.markdown("<h2><u>CI/CD (Continuous Integration/Continuous Delivery)</u></h2>", unsafe_allow_html = True)
        grid_3 = tech_cols1.columns(6)
        tech_stack(
            grid_3,
            ["Git", "GitHub", "FastAPI", "MLflow", "Docker"],
            [],
            tech_images
        )
        tech_cols2.markdown("<h2><u>Data Visualization / Software Development</u></h2>", unsafe_allow_html = True)
        grid_4 = tech_cols2.columns(6)
        tech_stack(
            grid_4,
            ["Plotly Dash", "Streamlit", "PyQt6"],
            [],
            tech_images
        )
        tech_cols2.markdown("<h2><u>Automation</u></h2>", unsafe_allow_html = True)
        grid_5 = tech_cols2.columns(6)
        tech_stack(
            grid_5,
            ["Selenium WebDriver", "PyAuto GUI", "BotCity", "Apache Airflow", "Luigi"],
            [],
            tech_images
        )
        tech_cols2.markdown("<h2><u>Cloud</u></h2>", unsafe_allow_html = True)
        grid_6 = tech_cols2.columns(6)
        tech_stack(
            grid_6,
            ["AWS", "Azure", "GCP"],
            [],
            tech_images
        )
        tech_cols2.markdown("<h2><u>Databases</u></h2>", unsafe_allow_html = True)
        grid_7 = tech_cols2.columns(6)
        tech_stack(
            grid_7,
            ["MySQL", "SQL Server"], 
            [],
            tech_images
        )
        tech_cols2.markdown("<h2><u>Languages</u></h2>", unsafe_allow_html = True)
        grid_8 = tech_cols2.columns(6)
        tech_stack(
            grid_8,
            ["Python", "Bash", "Go"], 
            [],
            tech_images
        )
        st.divider()
    with tabs_tech_stacks[1]: #CYBERSECURITY
        tech_cols = grid([2, 0.2, 2])
        tech_cols1 = tech_cols.container()
        tech_cols.container()
        tech_cols2 = tech_cols.container()
        tech_cols1.markdown("<h2><u>Virtual Machines & Operational Systems</u></h2>", unsafe_allow_html = True)
        grid_1 = tech_cols1.columns(6)
        tech_stack(
            grid_1,
            ["QEMU", "KALI Linux", "Ubuntu"],
            [],
            tech_images
        )
        tech_cols1.markdown("<h2><u>Automation</u></h2>", unsafe_allow_html = True)
        grid_2 = tech_cols1.columns(6)
        tech_stack(
            grid_2,
            ["Selenium WebDriver", "Apache Airflow", "Luigi"],
            [],
            tech_images
        )
        tech_cols1.markdown("<h2><u>Languages</u></h2>", unsafe_allow_html = True)
        grid_3 = tech_cols1.columns(6)
        tech_stack(
            grid_3,
            ["Python", "Bash", "Go"],
            [],
            tech_images
        )
        tech_cols1.markdown("<h2><u>Asset Discovery</u></h2>", unsafe_allow_html = True)
        grid_4 = tech_cols1.columns(6)
        tech_stack(
            grid_4,
            ["Shodan", "Censys"],
            [],
            tech_images
        )
        tech_cols1.markdown("<h2><u>Bug Bounty Platforms</u></h2>", unsafe_allow_html = True)
        grid_5 = tech_cols1.columns(6)
        tech_stack(
            grid_5,
            ["HackerOne", "BugCrowd", "Intigriti"],
            [],
            tech_images
        )
        tech_cols2.markdown("<h2><u>Vulnerability Assessment</u></h2>", unsafe_allow_html = True)
        grid_6 = tech_cols2.columns(6)
        tech_stack(
            grid_6,
            ["Metasploit", "Burp Suite", "NMAP", "Nikto", "Project Discovery Tools"],
            [],
            tech_images
        )
        tech_cols2_cols = tech_cols2.columns(2)
        tech_cols2_cols[0].markdown("<h3>Project Discovery Tools</h3>", unsafe_allow_html = True)
        project_discovery_tools = [
            "Nuclei",
            "Subfinder",
            "HTTPX",
            "DNSX",
            "Katana",
            "Naabu"
        ]
        for x in project_discovery_tools:
            tech_cols2_cols[0].markdown(f"* {x}")
        tech_cols2_cols[0].divider()
        tech_cols2_cols[0].markdown("<h3>Python Tools</h3>", unsafe_allow_html = True)
        python_tools = [
            "DNSReaper (Subdomain Takeover)",
            "GraphW00f (GraphQL fingerprint)",
            "Arjun (Hidden URL parameters)",
            "SSTImap (Template Injection)",
            "SQLmap (SQL Injection)",
            "SpyHunt",
            "CORSY (CORS Misconfiguration)",
            "XSRFProbe (Cross-Site Request Forgery - CSRF)",
            "XSStrike (XSS Scanner)",
            "FavFreak (Favicon)"
        ]
        for x in python_tools:
            tech_cols2_cols[0].markdown(f"* {x}")
        tech_cols2_cols[0].divider()
        tech_cols2_cols[1].markdown("<h3>Go Tools</h3>", unsafe_allow_html = True)
        go_tools = [
            "WayBackURLs",
            "FFuF (Fuzzer)",
            "Goctopus (GraphQL Fingerprint)",
            "TInjA (Template Injection)",
            "SURF (Server Side Request Forgery - SSRF)",
            "SmuggleFuzz (Request Smuggling)",
            "Gxss (XSS Scanner)",
            "DalFox (XSS Scanner)",
            "Subzy (Subdomain Takeover)",
            "MX-SPF Takeover (Subdomain Takeover)",
            "403jump (403 Status Code Bypass)",
            "Favirecon (Favicon)",
            "Shortscan (Windows IIS)",
            "Trufflehog (Credentials Scanner)"
        ]
        for x in go_tools:
            tech_cols2_cols[1].markdown(f"* {x}")
        tech_cols2_cols[1].divider()
        tech_cols2_cols[1].markdown("<h3>Other Tools</h3>", unsafe_allow_html = True)
        other_tools = [
            "Trivy (Credentials & Security Scanner)"
        ]
        for x in other_tools:
            tech_cols2_cols[1].markdown(f"* {x}")
        tech_cols2_cols[1].divider()


with tabs[3]:
    st.markdown("<h1 style='text-align:center'>GitHub Projects</h1>",
                unsafe_allow_html = True)
    display_grid = grid([1, 4, 1], vertical_align = True)
    display_grid.container()
    display = display_grid.container()
    display_grid.container()
    projects_list = [
"""
<h2 style='text-align:center'>2024</h2>
""",
"""
<div style='font-size:35px'><b>
<a href='https://github.com/COELHOGenAI/'>
COELHO GenAI
</a><br>
<p>September 2024</p>
</b></div>
""",
"""
<div style='font-size:35px'><b>
<a href='https://github.com/PentestingAutomation/'>
Pentesting Automation
</a><br>
<p>July 2024</p>
</b></div>
""",
#----------------------------------------
    """
<h2 style='text-align:center'>2023</h2>
""",
    """
<div style='font-size:35px'><b>
<a href='https://coelhovision.streamlit.app/'>
COELHO VISION
</a><br>
<p>December 2023</p>
</b></div>
""",
    """
<div style='font-size:35px'><b>
<a href='https://f1analytics.streamlit.app/'>
Formula 1 Analytics
</a><br>
<p>December 2023</p>
</b></div>
""",
    """
<div style='font-size:35px'><b>
<a href='https://coelhofinance.streamlit.app/'>
COELHO Finance
</a><br>
<p>September 2023</p>
</b></div><hr>
""",
#----------------------------------------
    """
<h2 style='text-align:center'>2022</h2>
""",
    """
<div style='font-size:35px'><b>
<a href='https://github.com/rafaelcoelho1409/DataEngineering'>
Data Engineering and Machine Learning with Airflow & PySpark
</a><br>
<p>April 2022</p>
</b></div>
""",
    """
<div style='font-size:35px'><b>
<a href='https://github.com/rafaelcoelho1409/DataEngineering2'>
Data Engineering and Machine Learning with Airflow, Pandas, SARIMAX and XGBoost
</a><br>
<p>April 2022</p>
</b></div>
""",
    """
<div style='font-size:35px'><b>
<a href='https://github.com/rafaelcoelho1409/TimeSeriesForecast'>
Time Series & Forecast using SARIMAX, XGBoost and Facebook Prophet
</a><br>
<p>March 2022</p>
</b></div>
""",
    """
<div style='font-size:35px'><b>
<a href='https://github.com/rafaelcoelho1409/NLP-WebScraping'>
Natural Language Processing (NLP) & Web Scraping
</a><br>
<p>March 2022</p>
</b></div>
""",
    """
<div style='font-size:35px'><b>
<a href='https://github.com/rafaelcoelho1409/ComputerVision'>
Computer Vision with Tensorflow, Keras and OpenCV
</a><br>
<p>January 2022</p>
</b></div>
""",
    """
<div style='font-size:35px'><b>
<a href='https://github.com/rafaelcoelho1409/DeepLearning'>
Deep Learning using Tensorflow & Keras
</a><br>
<p>January 2022</p>
</b></div><hr>
""",
    """
<h2 style='text-align:center'>2021</h2>
""",
    """
<div style='font-size:35px'><b>
<a href='https://github.com/rafaelcoelho1409/CustomerSegmentation'>
Customer segmentation using clustering algorithms (Machine Learning)
</a><br>
<p>November 2021</p>
</b></div>
""",
    """
<div style='font-size:35px'><b>
<a href='https://github.com/rafaelcoelho1409/GoogleShoppingBot'>
Web Scraping with Selenium to collect product prices on Google Shopping
</a><br>
<p>November 2021</p>
</b></div>
""",
    """
<div style='font-size:35px'><b>
<a href='https://github.com/rafaelcoelho1409/Computer_Vision_AI_1'>
Detecting and classifying objects using Computer Vision and Deep Learning
</a><br>
<p>May 2021</p>
</b></div>
""",
    """
<div style='font-size:35px'><b>
<a href='https://github.com/rafaelcoelho1409/Chest-X-Ray-COVID-19'>
X-ray images for detection of COVID-19 or pneumonia
</a><br>
<p>March 2021</p>
</b></div><hr>
""",
    ]
    scrollable_content = "".join(projects_list)
    create_scrollable_section(scrollable_content, display, "600px")
    ###############################################
