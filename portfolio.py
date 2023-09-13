import streamlit as st
from streamlit_extras.grid import grid

st.set_page_config(
    page_title = "Rafael Silva Coelho - Portfolio",
    layout = "wide"
)

st.latex("\\Huge{\\underline{\\textbf{Rafael Silva Coelho - PORTFOLIO}}}")

grid1 = grid([4, 1], vertical_align = True)
container1 = grid1.container()
container2 = grid1.container()
container2.image("rafael_coelho_photo.jpeg")
container1.markdown("""<div style='font-size:28px'>
                    &#8226 Data Scientist and AI Engineer with over 3 years of experience in the industry.<br>
                    &#8226 Highly proficient in Data Science, Machine Learning, 
                    Computer Vision, Natural Language Processing, Reinforcement Learning, and Data Engineering.<br>
                    &#8226 Developing and deploying machine learning models to solve real-world problems,
                    such as predictive models, anomaly detection and other models to be applied in industry areas,
                    such as Finance, Marketing, Commodities, Retail etc.<br>
                    &#8226 Actually working in one of the Big Four companies for over a year.<br><br>
        </div>""",
        unsafe_allow_html = True)
main_areas = [
    "Data Science",
    "Data Engineering",
    "Data Analytics",
    "Machine Learning",
    "Automation (RPA)",
    "Artificial Intelligence",
    "Computer Vision"
]
st.write("$$\\large{\\textbf{My areas of expertise}}$$")
grid3 = grid(len(main_areas))
for x in main_areas:
    grid3.write("$$\\textbf{" + x + "}$$")
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
st.latex("\\Huge{\\textbf{COELHO Finance}}")
grid2 = grid([1, 4])
container3 = grid2.container()
container4 = grid2.container()
container3.image("coelho_finance_logo.png")
container3.markdown("""
    <h1>
    <a 
        style='text-align:center'
        href='https://coelhofinance.streamlit.app/'>
    COELHO Finance
    </a>
    </h1>""",
    unsafe_allow_html = True)
container4.markdown("""<div style='font-size:28px'>
                    Get to know <a href='https://coelhofinance.streamlit.app'>COELHO Finance</a>,
                    a new powerful tool to help you make informed investment decisions, 
                    track your investments and identify opportunities. With COELHO Finance, 
                    you can have the confidence to take control of your finances 
                    and achieve your investment goals.<br><br>
                    This Financial Market platform was developed with the intention of being a 
                    personal portfolio project to test lots of Data Science, Machine Learning
                    and Artificial Intelligence tools and frameworks applied to Financial Market. 
                    For now, the access to the platform is free.
        </div>""",
        unsafe_allow_html = True)
with st.expander(
    label = "COELHO Finance",
    expanded = True
):
    cols = grid(5)
    for i in range(1, 6):
        cols.image(f"coelhofinance{i}.png")
st.divider()
cols = st.columns(2)
with cols[0]:
    st.latex("\\Huge{\\textbf{Tech Stack / Skills}}")
    st.write("$$\\Large{\\underline{\\textbf{Languages}}}$$")
    languages_image = grid(6)
    languages_desc = grid(6)
    languages_image.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png",
    )
    languages_desc.caption("$$\\textbf{Python}$$")
    st.write("$$\\Large{\\underline{\\textbf{Artificial Intelligence / Machine Learning}}}$$")
    dsai_image = grid(6)
    dsai_desc = grid(6)
    for x in zip([
        "https://avatars.githubusercontent.com/u/15658638?s=280&v=4",
        "https://pytorch.org/tutorials/_static/img/thumbnails/cropped/profiler.png",
        "https://static.javatpoint.com/tutorial/keras/images/keras.png",
        "https://cdn-images-1.medium.com/v2/resize:fit:889/format:png/1*TN3K15kcQUDYPsl8SM5DcA.png",
        "https://miro.medium.com/v2/resize:fit:720/1*yhE3CBwTrlXcAIvNJNTQiA.png",
        "https://cdn.dribbble.com/users/3752/screenshots/3302280/attachments/712571/prophet-logo-red.png",
    ], [
        "$$\\textbf{Tensorflow}$$",
        "$$\\textbf{PyTorch}$$",
        "$$\\textbf{Keras}$$",
        "$$\\textbf{Scikit-Learn}$$",
        "$$\\textbf{XGBoost}$$",
        "$$\\textbf{Prophet}$$",
    ]):
        dsai_image.image(x[0])
        dsai_desc.caption(x[1])
    dsai_image = grid(6)
    dsai_desc = grid(6)
    for x in zip([
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/OpenCV_Logo_with_text_svg_version.svg/800px-OpenCV_Logo_with_text_svg_version.svg.png",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1y_jz77iMIbgVRQ6JEs2YlSSbJs_j0zNEhr5N_Zh2XZxq5bCtZf81lw2UWnoWlD65r-U",
        "https://images.squarespace-cdn.com/content/v1/56e2e0c520c6472a2586add2/1593683608007-L71NCKC2O54GFBHPB0W9/CP%2BLogos%2B2%2B%25288%2529.jpg",
    ], [
        "$$\\textbf{OpenCV}$$",
        "$$\\textbf{NLTK}$$",
        "$$\\textbf{Transformers}$$",
    ]):
        dsai_image.image(x[0])
        dsai_desc.caption(x[1])
    st.write("$$\\Large{\\underline{\\textbf{Data Science}}}$$")
    ds_image = grid(6)
    ds_desc = grid(6)
    for x in zip([
        "https://miro.medium.com/v2/resize:fit:1001/1*vPezx00A1u0WAfS8e8wBXQ.png",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwbEmQTbGryUhOqEhjFHWbRonjX9GU0Qoe7c9DL5q_wp18fpdU7RK8tvd9YVqnntgRESA",
        "https://store-images.s-microsoft.com/image/apps.36868.bfb0e2ee-be9e-4c73-807f-e0a7b805b1be.712aff5d-5800-47e0-97be-58d17ada3fb8.a46845e6-ce94-44cf-892b-54637c6fcf06",
        "https://www.cienciaedados.com/wp-content/uploads/2023/08/pyspark.jpg",
        "https://raw.githubusercontent.com/pola-rs/polars-static/master/web/splash.png"
    ], [
        "$$\\textbf{NumPy}$$",
        "$$\\textbf{Pandas}$$",
        "$$\\textbf{Plotly}$$",
        "$$\\textbf{PySpark}$$",
        "$$\\textbf{Polars}$$",
    ]):
        ds_image.image(x[0])
        ds_desc.caption(x[1])
    st.write("$$\\Large{\\underline{\\textbf{Frameworks}}}$$")
    frameworks_image = grid(6)
    frameworks_desc = grid(6)
    for x in zip([
        "https://miro.medium.com/v2/resize:fit:400/1*hX_l9M_WJkaupAwEwB7mZQ.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png",
        "https://res.cloudinary.com/practicaldev/image/fetch/s--me_F8s1R--/c_imagga_scale,f_auto,fl_progressive,h_1080,q_auto,w_1080/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zarel6bkijh9o4nz596n.png",
        "https://miro.medium.com/v2/resize:fit:500/1*GQnwZB95_StaHm_dCE6Bow.png",
        "https://miro.medium.com/v2/resize:fit:1000/1*0zMGy7YdRhuSA3X2ymqotg.jpeg",
        "https://images.crunchbase.com/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/ywjqppks5ffcnbfjuttq"
    ], [
        "$$\\textbf{Git}$$",
        "$$\\textbf{GitHub}$$",
        "$$\\textbf{FastAPI}$$",
        "$$\\textbf{Airflow}$$",
        "$$\\textbf{MLflow}$$",
        "$$\\textbf{Docker}$$",
    ]):
        frameworks_image.image(x[0])
        frameworks_desc.caption(x[1])
    st.write("$$\\Large{\\underline{\\textbf{Data Visualization}}}$$")
    ds_image = grid(6)
    ds_desc = grid(6)
    for x in zip([
        "https://www.pngitem.com/pimgs/m/499-4995557_plotly-dash-logo-png-transparent-png.png",
        "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png"
    ], [
        "$$\\textbf{Plotly Dash}$$",
        "$$\\textbf{Streamlit}$$",
    ]):
        ds_image.image(x[0])
        ds_desc.caption(x[1])
    st.write("$$\\Large{\\underline{\\textbf{Web Scraping \& Automation}}}$$")
    ds_image = grid(6)
    ds_desc = grid(6)
    for x in zip([
        "https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png",
        "https://codetorial.net/pyautogui/_images/logo.jpg",
        "https://pbs.twimg.com/profile_images/1374747222353575944/7kS6IhZb_400x400.jpg"
    ], [
        "$$\\textbf{Selenium}$$",
        "$$\\textbf{PyAutoGUI}$$",
        "$$\\textbf{BotCity}$$",
    ]):
        ds_image.image(x[0])
        ds_desc.caption(x[1])
    st.write("$$\\Large{\\underline{\\textbf{Cloud}}}$$")
    ds_image = grid(6)
    ds_desc = grid(6)
    for x in zip([
        "https://www.nafcu.org/sites/default/files/styles/200_y/public/2018-06/Partner%20Logos-35.png?itok=lGsk2DUF",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Microsoft_Azure.svg/1200px-Microsoft_Azure.svg.png"
    ], [
        "$$\\textbf{AWS}$$",
        "$$\\textbf{Azure}$$",
    ]):
        ds_image.image(x[0])
        ds_desc.caption(x[1])
    st.write("$$\\Large{\\underline{\\textbf{Databases}}}$$")
    ds_image = grid(6)
    ds_desc = grid(6)
    for x in zip([
        "https://www.tshirtgeek.com.br/wp-content/uploads/2021/08/com031.jpg",
        "https://cdn-icons-png.flaticon.com/512/5968/5968364.png"
    ], [
        "$$\\textbf{MySQL}$$",
        "$$\\textbf{SQL Server}$$",
    ]):
        ds_image.image(x[0])
        ds_desc.caption(x[1])
with cols[1]:
    st.latex("\\Huge{\\textbf{Projects}}")
    st.latex("\\Large{\\textbf{2023}}")
    with st.expander(
        label = "",
        expanded = True
    ):
        st.subheader("COELHO Finance")
        st.write("September 2023")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://coelhofinance.streamlit.app'>
                    Access Platform
                    </a>""",
                    unsafe_allow_html = True)
    st.latex("\\Large{\\textbf{2022}}")
    with st.expander(
        label = "",
        expanded = True
    ):
        st.subheader("Data Engineering and Machine Learning with Airflow & PySpark")
        st.write("April 2022")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://github.com/rafaelcoelho1409/DataEngineering'>
                    Github Repository
                    </a>""",
                    unsafe_allow_html = True)
        st.divider()
        st.subheader("Data Engineering and Machine Learning with Airflow, Pandas, SARIMAX and XGBoost")
        st.write("April 2022")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://github.com/rafaelcoelho1409/DataEngineering2'>
                    Github Repository
                    </a>""",
                    unsafe_allow_html = True)
        st.divider()
        st.subheader("Time Series & Forecast using SARIMAX, XGBoost and Facebook Prophet")
        st.write("March 2022")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://github.com/rafaelcoelho1409/TimeSeriesForecast'>
                    Github Repository
                    </a>""",
                    unsafe_allow_html = True)
        st.divider()
        st.subheader("Natural Language Processing (NLP) & Web Scraping")
        st.write("March 2022")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://github.com/rafaelcoelho1409/NLP-WebScraping'>
                    Github Repository
                    </a>""",
                    unsafe_allow_html = True)
        st.divider()
        st.subheader("Computer Vision with Tensorflow, Keras and OpenCV")
        st.write("January 2022")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://github.com/rafaelcoelho1409/ComputerVision'>
                    Github Repository
                    </a>""",
                    unsafe_allow_html = True)
        st.divider()
        st.subheader("Deep Learning using Tensorflow & Keras")
        st.write("January 2022")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://github.com/rafaelcoelho1409/DeepLearning'>
                    Github Repository
                    </a>""",
                    unsafe_allow_html = True)
        st.divider()
    st.latex("\\Large{\\textbf{2021}}")
    with st.expander(
        label = "",
        expanded = True
    ):
        st.subheader("Customer segmentation using clustering algorithms (Machine Learning)")
        st.write("November 2021")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://github.com/rafaelcoelho1409/CustomerSegmentation'>
                    Github Repository
                    </a>""",
                    unsafe_allow_html = True)
        st.divider()
        st.subheader("Web Scraping with Selenium to collect product prices on Google Shopping")
        st.write("November 2021")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://github.com/rafaelcoelho1409/GoogleShoppingBot'>
                    Github Repository
                    </a>""",
                    unsafe_allow_html = True)
        st.divider()
        st.subheader("Detecting and classifying objects using Computer Vision and Deep Learning")
        st.write("May 2021")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://github.com/rafaelcoelho1409/Computer_Vision_AI_1'>
                    Github Repository
                    </a>""",
                    unsafe_allow_html = True)
        st.divider()
        st.subheader("X-ray images for detection of COVID-19 or pneumonia")
        st.write("March 2021")
        st.markdown("""
                    <a
                    style='font-size:25px; text-align:center'
                    href='https://github.com/rafaelcoelho1409/Chest-X-Ray-COVID-19'>
                    Github Repository
                    </a>""",
                    unsafe_allow_html = True)
        st.divider()