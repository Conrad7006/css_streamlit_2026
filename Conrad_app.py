import streamlit as st
#import pandas as pd
# import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "STEM Data Explorer", "Hobbies"],
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
    st.write("My project is about creating a holistic framework for process simulaiton")
    st.write("The figure below shows the proposed framework. Each modular section can be swopped for different models in a library.")
    st.write("The yellow puzzle pieces show hich sections my project will have different models for")
    st.write("To date, two process models have been written with the goal of simulating a concentration plant")
    
    st.image("Assets/Framework.jpg")
    
    st.sidebar.header("Model Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a implemented model to explore", 
        ["Milling model", "Flotation model", "Crusher model"]
    )

    if data_option == "Milling model":
        st.write("### The Mill and Hydrocyclone Circuit")
        st.write("Below is a figure that shows the mill and hydrocyclone circuit.")
        st.image("Assets/Mill_circuit.png")
        
        st.write("The Hulbert model, as implemented by Le Roux et al. 2013, has been validated in this work. The two graphs below can be compared")
        st.image("Assets/Mill_original.png", caption = "From Le Roux et al. 2013")
        st.image("Assets/Mill_compare.png", caption = "From this work")

    elif data_option == "Flotation model":
        st.write("### The Flotation Bank")
        st.write("Below is a figure that shows the four cell flotation bank. There are also three sumps, one inlet and two outlet.")
        st.image("Assets/Float_circuit.png")
        
        st.write("The model from Auret et al. 2025 was implemented into Julia and the sump tank response to step changes can be compared below.")
        st.image("Assets/Float_original.png", caption = "From Auret et al. 2025")
        st.image("Assets/Float_compare.png", caption = "From this work")

    elif data_option == "Crusher model":
        st.write("### The Cone Crusher")
        st.write("The figure below shows a cone crusher. This crusher type is the most common used in industry")
        st.image("Assets/Crush_pic.png")
        
        st.write("The figure below shows the Whiten model. This model will be used in this work for the crusher model.")
        st.write("The model contains the selection function (S), which determines the outflow, and the breakage fucntion (B) which describes the crushing of the ore within the cursher.")
        st.image("Assets/Crush_circuit.png")

elif menu == "Hobbies":
    # Add a contact section
    st.header("Contact Information")
    email = "jane.doe@example.com"
    st.write(f"You can reach me at {email}.")