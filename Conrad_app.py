import streamlit as st
#import pandas as pd
# import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "STEM Data Explorer", "Contact"],
)

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Mr. Conrad Dawid Kriel"
    field = "Process control and monitoring"
    institution = "Stellenbosch University"
    contact = "25056778@sun.ac.za"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.write(f"Can be contacted at: {contact}")
    
    st.image("Assets/Degree.jpg", caption="Official Certificate")

elif menu == "STEM Data Explorer":
    st.title("Results from my project to date")
    st.sidebar.header("Model Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a implemented model to explore", 
        ["Milling model", "Flotation model", "Crusher model"]
    )

    if data_option == "Milling model":
        st.write("### The Mill Implementation")


    elif data_option == "Flotation model":
        st.write("### The Flotation Bank")
 

    elif data_option == "Crusher model":
        st.write("### The Cone Crusher")


elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "jane.doe@example.com"
    st.write(f"You can reach me at {email}.")