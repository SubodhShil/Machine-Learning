import streamlit as st
import pandas as pd
import numpy as np


# Application Title
st.write("# Mutli Modal AI Chat Application")


def gradient_div(content, bg, page_link):
    features_section = f"""
        <a href="{page_link}" target="_self" style="
            height: 60px;
            width: 100%;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            display: inline-block;
            text-align: center;
            flex-direction: column;
            color: white;
            font-size: 16px;
            font-weight: 600;
            background: {bg};
            align-items: center;
            justify-content: center;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            text-decoration: none;
        ">
            {content}
        </a>
    """
    return features_section


# Use the function in your Streamlit app:

st.markdown(
    gradient_div(
        "Generate AI Arts",
        "linear-gradient(to right, #fc4a1a, #f7b733)",
        "/AI_Art"
    ),
    unsafe_allow_html=True
)

st.markdown(
    gradient_div(
        "Grammar Check",
        "linear-gradient(to right, #00f260, #0575e6)",
        "/Grammar_Check"
    ),
    unsafe_allow_html=True
)

st.markdown(
    gradient_div(
        "Image to PDF",
        "linear-gradient(to right, #74ebd5, #acb6e5)",
        "/Image_To_PDF"
    ),
    unsafe_allow_html=True
)


st.markdown(
    gradient_div(
        "Text To Voice",
        "linear-gradient(to right, #fc354c, #0abfbc)",
        "/Image_To_PDF"
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
