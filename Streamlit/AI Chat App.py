import streamlit as st
import pandas as pd
import numpy as np

# Add custom CSS with Google Fonts
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,100..900;1,100..900&family=Karla:ital,wght@0,200..800;1,200..800&family=Raleway:ital,wght@0,100..900;1,100..900&family=Sofia+Sans:ital,wght@0,1..1000;1,1..1000&display=swap');

html, body, [class*="css"] {
    font-family: "Archivo", sans-serif;
}

.stApp {
    font-family: "Archivo", sans-serif;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Archivo', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# Application Title
st.write("# Mutli Modal AI Chat Application")


def gradient_div(content, bg, page_link):
    features_section = f"""
        <a href="{page_link}" target="_self" style="
            height: 70px;
            width: 100%;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 25px;
            display: flex;
            text-align: center;
            flex-direction: column;
            color: white;
            font-size: 18px;
            font-weight: 600;
            background: {bg};
            align-items: center;
            justify-content: center;
            box-shadow: 0px 8px 16px rgba(0,0,0,0.1);
            text-decoration: none;
            transition: all 0.3s ease;
        ">
            {content}
        </a>
        <style> 
            a:hover {{
                transform: translateY(-3px);
                box-shadow: 0px 12px 24px rgba(0,0,0,0.15);
            }}
        </style>
    """
    return features_section


# Use the function in your Streamlit app:

# Create a 2-column layout
col1, col2 = st.columns(2)

# Place boxes in columns
with col1:
    st.markdown(
        gradient_div(
            "Generate AI Arts",
            "linear-gradient(to right, #FF416C, #FF4B2B)",
            "/AI_Art"
        ),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        gradient_div(
            "Grammar Check",
            "linear-gradient(to right, #4776E6, #8E54E9)",
            "/Grammar_Check"
        ),
        unsafe_allow_html=True
    )

# Second row
with col1:
    st.markdown(
        gradient_div(
            "Image to Text",
            "linear-gradient(to right, #11998e, #38ef7d)",
            "/Image_To_Text"
        ),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        gradient_div(
            "Multi-Modal AI Chat",
            "linear-gradient(to right, #2980B9, #6DD5FA)",
            "/Multi_Modal_AI"
        ),
        unsafe_allow_html=True
    )


# Sidebar
api_method = st.sidebar.selectbox(
    '### API Methods',
    ('Freemium', 'Your Own API')
)


if api_method == 'Freemium':
    model = st.sidebar.selectbox(
        'Select Model',
        ('Gemini', 'Mistral', 'DeepSeek')
    )
    st.sidebar.write(f"Selected model: {model}")

else:
    api_input = st.sidebar.text_input(
        "Enter your API key", key="api_input", type="password")
