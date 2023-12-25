import streamlit as st
from streamlit_extras.grid import grid
import base64
import json
from functions import (
    image_border_radius,
    image_border_radius_url,
    display_text_in_colored_square,
    create_scrollable_section
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
    image_border_radius("./assets/rafael_coelho_1.jpeg", 20, 100, 100, container2)
    container1.markdown("""<div style='font-size:25px'>
                        &#8226 Data Scientist and Machine Learning Engineer with over 3 years of experience in the industry.<br>
                        &#8226 Highly proficient in Data Science, Machine Learning, 
                        Computer Vision, Natural Language Processing, Reinforcement Learning, and Data Engineering.<br>
                        &#8226 Developing and deploying machine learning models to solve real-world problems,
                        such as predictive models, anomaly detection and other models to be applied in industry areas,
                        such as Finance, Marketing, Commodities, Retail etc.<br>
                        &#8226 Recently worked in one of the Big Four companies for over a year.<br><br><br>
            </div>""",
            unsafe_allow_html = True)
    cols = container1.columns(2)
    with cols[0]:
        st.markdown("""
            <h1>
            <a 
                style='text-align:center'
                href='https://www.linkedin.com/in/rafaelcoelho1409/'>
            LinkedIn
            </a>
            </h1>""",
            unsafe_allow_html = True)
    with cols[1]:
        st.markdown("""
            <h1>
            <a 
                style='text-align:center'
                href='https://github.com/rafaelcoelho1409'>
            GitHub
            </a>
            </h1>""",
            unsafe_allow_html = True)
    st.divider()


    #MY AREAS OF EXPERTISE
    main_areas = [
        "Data<br>Science",
        "Data<br>Engineering",
        "Data<br>Analytics",
        "Machine<br>Learning",
        "Automation<br>(RPA)",
        "Artificial<br>Intelligence",
        "Anomaly<br>Detection",
        "Computer<br>Vision"
    ]
    st.markdown("<i><h2 style='text-align:center'>My areas of expertise</h2></i>",
                unsafe_allow_html = True)
    grid3 = grid(len(main_areas))
    for x in main_areas:
        display_text_in_colored_square(
            f"<h3>{x}</h3>",
            grid3,
            "gray")
    st.divider()


with tabs[1]: #PORTFOLIO PROJECTS
    st.markdown("<h1 style='text-align:center'>Portfolio Projects</h1>",
                unsafe_allow_html = True)
    st.divider()
    style1 = grid([1, 0.2, 3])
    image1 = style1.container()
    image_border_radius_url(
        "./assets/coelho_finance_logo.png",
        "https://coelhofinance.streamlit.app/",
        20, 100, 100, image1)
    style1.container()
    description1 = style1.container()
    description1.write("$$\\Huge{\\textbf{COELHO Finance}}$$")
    description1.markdown("""<div style='font-size:20px'>
                        Get to know <a href='https://coelhofinance.streamlit.app'>COELHO Finance</a>,
                        a new powerful tool to help you make informed investment decisions, 
                        track your investments and identify opportunities. With COELHO Finance, 
                        you can have the confidence to take control of your finances 
                        and achieve your investment goals.<br><br>
                        This Financial Market platform was developed with the intention of being a 
                        personal portfolio project to test lots of Data Science, Machine Learning
                        and Artificial Intelligence tools and frameworks applied to Financial Market. 
                        For now, the access to the platform is free.</div>""", unsafe_allow_html = True)
    with st.expander(
        label = "COELHO Finance",
        expanded = True
    ):
        cols = st.columns(10)
        for i in range(0, 10):
            with cols[i]:
                st.image(f"./assets/coelhofinance{i+1:0>2}.png")
    st.divider()
    style2 = grid([1, 0.2, 3])
    image2 = style2.container()
    image_border_radius_url(
        "./assets/f1_home.jpg",
        "https://f1analytics.streamlit.app/",
        20, 100, 100, image2)
    style2.container()
    description2 = style2.container()
    description2.write("$$\\Huge{\\textbf{Formula 1 Analytics}}$$")
    description2.markdown("""<div style='font-size:20px'>
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
    with st.expander(
        label = "Formula 1 Analytics",
        expanded = True
    ):
        cols = st.columns(10)
        for i in range(0, 10):
            with cols[i]:
                st.image(f"./assets/f1analytics{i+1:0>2}.png")
    st.divider()


with tabs[2]: #TECH STACKS / SKILLS
    tech_images = json.load(open("tool_images.json"))
    st.markdown("<h1 style='text-align:center'>Tech Stacks / Skills</h1>",
                unsafe_allow_html = True)
    st.divider()
    tech_cols = grid([2, 0.2, 2])
    tech_cols1 = tech_cols.container()
    tech_cols.container()
    tech_cols2 = tech_cols.container()


    tech_cols1.markdown("<h2><u>Artificial Intelligence / Machine Learning</u></h2>", unsafe_allow_html = True)
    grid_1 = tech_cols1.columns(6)
    for tech_list in (
        ["TensorFlow", "PyTorch", "Keras", "Scikit Learn", "XGBoost", "Neural Prophet"],
        [" NLTK", "Hugging Face Transformers", " ADTK", "Statsmodels"]):
        for i, tech in enumerate(tech_list):
            with grid_1[i]:
                if tech_images[tech].startswith("http"):
                    image_border_radius(tech_images[tech], 10, 100, 100, is_html = True)
                    st.caption(tech)
                else:
                    display_text_in_colored_square(
                        f"<h4>{tech.replace(' ', '<br>')}</h4>",
                        background_color = "black")
                    st.caption(tech_images[tech])
    tech_cols1.markdown("<h2><u>Computer Vision</u></h2>", unsafe_allow_html = True)
    grid_1 = tech_cols1.columns(6)
    for tech_list in (
        ["OpenCV", "Ultralytics", "MediaPipe"], []):
        for i, tech in enumerate(tech_list):
            with grid_1[i]:
                if tech_images[tech].startswith("http"):
                    image_border_radius(tech_images[tech], 10, 100, 100, is_html = True)
                    st.caption(tech)
                else:
                    display_text_in_colored_square(
                        f"<h4>{tech.replace(' ', '<br>')}</h4>",
                        background_color = "black")
                    st.caption(tech_images[tech])
    tech_cols1.markdown("<h2><u>Data Science & Data Engineering</u></h2>", unsafe_allow_html = True)
    grid_2 = tech_cols1.columns(6)
    for tech_list in (
        ["NumPy", "Pandas", "Plotly", "PySpark", "Polars"], []):
        for i, tech in enumerate(tech_list):
            with grid_2[i]:
                if tech_images[tech].startswith("http"):
                    image_border_radius(tech_images[tech], 10, 100, 100, is_html = True)
                    st.caption(tech)
                else:
                    display_text_in_colored_square(
                        f"<h4>{tech.replace(' ', '<br>')}</h4>",
                        background_color = "black")
                    st.caption(tech_images[tech])
    tech_cols1.markdown("<h2><u>CI/CD (Continuous Integration/Continuous Delivery)</u></h2>", unsafe_allow_html = True)
    grid_3 = tech_cols1.columns(6)
    for tech_list in (
        ["Git", "GitHub", "FastAPI", "Apache Airflow", "MLflow", "Docker"], []):
        for i, tech in enumerate(tech_list):
            with grid_3[i]:
                if tech_images[tech].startswith("http"):
                    image_border_radius(tech_images[tech], 10, 100, 100, is_html = True)
                    st.caption(tech)
                else:
                    display_text_in_colored_square(
                        f"<h4>{tech.replace(' ', '<br>')}</h4>",
                        background_color = "black")
                    st.caption(tech_images[tech])
    tech_cols2.markdown("<h2><u>Data Visualization</u></h2>", unsafe_allow_html = True)
    grid_4 = tech_cols2.columns(6)
    for tech_list in (
        ["Plotly Dash", "Streamlit"], []):
        for i, tech in enumerate(tech_list):
            with grid_4[i]:
                if tech_images[tech].startswith("http"):
                    image_border_radius(tech_images[tech], 10, 100, 100, is_html = True)
                    st.caption(tech)
                else:
                    display_text_in_colored_square(
                        f"<h4>{tech.replace(' ', '<br>')}</h4>",
                        background_color = "black")
                    st.caption(tech_images[tech])
    tech_cols2.markdown("<h2><u>Web Scraping & Automation</u></h2>", unsafe_allow_html = True)
    grid_5 = tech_cols2.columns(6)
    for tech_list in (
        ["Selenium WebDriver", "PyAuto GUI", "BotCity"], []):
        for i, tech in enumerate(tech_list):
            with grid_5[i]:
                if tech_images[tech].startswith("http"):
                    image_border_radius(tech_images[tech], 10, 100, 100, is_html = True)
                    st.caption(tech)
                else:
                    display_text_in_colored_square(
                        f"<h4>{tech.replace(' ', '<br>')}</h4>",
                        background_color = "black")
                    st.caption(tech_images[tech])
    tech_cols2.markdown("<h2><u>Cloud</u></h2>", unsafe_allow_html = True)
    grid_6 = tech_cols2.columns(6)
    for tech_list in (
        ["AWS", "Azure", "GCP"], []):
        for i, tech in enumerate(tech_list):
            with grid_6[i]:
                if tech_images[tech].startswith("http"):
                    image_border_radius(tech_images[tech], 10, 100, 100, is_html = True)
                    st.caption(tech)
                else:
                    display_text_in_colored_square(
                        f"<h4>{tech.replace(' ', '<br>')}</h4>",
                        background_color = "black")
                    st.caption(tech_images[tech])
    tech_cols2.markdown("<h2><u>Databases</u></h2>", unsafe_allow_html = True)
    grid_7 = tech_cols2.columns(6)
    for tech_list in (
        ["MySQL", "SQL Server"], []):
        for i, tech in enumerate(tech_list):
            with grid_7[i]:
                if tech_images[tech].startswith("http"):
                    image_border_radius(tech_images[tech], 10, 100, 100, is_html = True)
                    st.caption(tech)
                else:
                    display_text_in_colored_square(
                        f"<h4>{tech.replace(' ', '<br>')}</h4>",
                        background_color = "black")
                    st.caption(tech_images[tech])
    tech_cols2.markdown("<h2><u>Languages</u></h2>", unsafe_allow_html = True)
    grid_8 = tech_cols2.columns(6)
    for tech_list in (
        ["Python"], []):
        for i, tech in enumerate(tech_list):
            with grid_8[i]:
                if tech_images[tech].startswith("http"):
                    image_border_radius(tech_images[tech], 10, 100, 100, is_html = True)
                    st.caption(tech)
                else:
                    display_text_in_colored_square(
                        f"<h4>{tech.replace(' ', '<br>')}</h4>",
                        background_color = "black")
                    st.caption(tech_images[tech])
    st.divider()


with tabs[3]:
    st.markdown("<h1 style='text-align:center'>GitHub Projects</h1>",
                unsafe_allow_html = True)
    display_grid = grid([1, 4, 1], vertical_align = True)
    display_grid.container()
    display = display_grid.container()
    display_grid.container()
    projects_list = [
    """
<h2 style='text-align:center'>2023</h2>
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