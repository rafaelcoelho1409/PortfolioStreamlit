import streamlit as st
import base64

def image_border_radius(image_path, border_radius, width, height, page_object = None, is_html = False):
    if is_html == False:
        with open(image_path, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode()
        # Create HTML string with the image
        img_html = f'<img src="data:image/jpeg;base64,{img_base64}" style="border-radius: {border_radius}px; width: {width}%; height: {height}%">'
        # Display the HTML string in Streamlit
        if page_object == None:
            st.markdown(img_html, unsafe_allow_html=True)
        else:
            page_object.markdown(img_html, unsafe_allow_html=True)
    else:
        # Create HTML string with the image
        img_html = f'<img src="{image_path}" style="border-radius: {border_radius}px; width: {width}%; height: {height}%">'
        # Display the HTML string in Streamlit
        if page_object == None:
            st.markdown(img_html, unsafe_allow_html=True)
        else:
            page_object.markdown(img_html, unsafe_allow_html=True)

def image_border_radius_url(
    image_path,
    url,
    border_radius, 
    width, 
    height, 
    page_object = None, 
    is_html = False):
    if is_html == False:
        with open(image_path, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode()
        # Create HTML string with the image
        img_html = f'<a href="{url}"><img src="data:image/jpeg;base64,{img_base64}" style="border-radius: {border_radius}px; width: {width}%; height: {height}%">'
        # Display the HTML string in Streamlit
        if page_object == None:
            st.markdown(img_html, unsafe_allow_html=True)
        else:
            page_object.markdown(img_html, unsafe_allow_html=True)
    else:
        # Create HTML string with the image
        img_html = f'<img src="{image_path}" style="border-radius: {border_radius}px; width: {width}%; height: {height}%">'
        # Display the HTML string in Streamlit
        if page_object == None:
            st.markdown(img_html, unsafe_allow_html=True)
        else:
            page_object.markdown(img_html, unsafe_allow_html=True)


def display_text_in_colored_square(
    text,
    page_object = None,
    background_color = "gray",
    text_color = "white"):
    # Define the HTML and CSS for the colored square
    square_html = f"""
    <div style="
        background-color: {background_color};
        color: white;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        ">
        {text}
    </div>
    """
    if page_object == None:
        # Render the colored square with text in Streamlit
        st.markdown(square_html, unsafe_allow_html=True)
    else:
        # Render the colored square with text in Streamlit
        page_object.markdown(square_html, unsafe_allow_html=True)

def huge_divider():
    return st.markdown("""
<hr style="border:2px solid white; margin-top: 0.5em; margin-bottom: 0.5em"/>
""", unsafe_allow_html=True)

def create_scrollable_section(content, page_object = None, height="400px"):
    # Defining the HTML and CSS
    scrollable_section_html = f"""
    <div style="
        overflow-y: scroll;
        height: {height};
        border: 1px solid #ccc;
        padding: 10px;
        margin: 10px 0;
        ">
        {content}
    </div>
    """
    if page_object == None:
        return st.markdown(scrollable_section_html, unsafe_allow_html = True)
    else:
        return page_object.markdown(scrollable_section_html, unsafe_allow_html = True)
    
def tech_stack(
    grid,
    tech_list1,
    tech_list2,
    tech_images
):
    for tech_list in (
        tech_list1,
        tech_list2):
        for i, tech in enumerate(tech_list):
            with grid[i]:
                if tech_images[tech].startswith("http"):
                    image_border_radius(tech_images[tech], 10, 100, 100, is_html = True)
                    st.caption(tech)
                else:
                    display_text_in_colored_square(
                        f"<h4>{tech.replace(' ', '<br>')}</h4>",
                        background_color = "black")
                    st.caption(tech_images[tech])
      