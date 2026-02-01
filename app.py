import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Mr. Napo Matsietsi"
field = "Dog Sciences"
institution = "University of Doggz"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "dog_03.jpg",
    caption="Dog classes (Breed 01)"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")
    if uploaded_file is not None:
        # User uploaded a file
        df = pd.read_csv(uploaded_file)
        st.success("Using uploaded CSV")
    else:
        df = pd.read_csv("dog_walking_publications_index_v5_realistic_growth.csv")
        st.info("Using default CSV included with the app")
        st.dataframe(publications)

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
dog_data = pd.DataFrame({
    "Experiment": ["Labrador", "Pitbull", "German Sheperd", "Golden Retriver", "Poodle"],
    "Dog Age (years)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

owner_data = pd.DataFrame({
    "Dog Owner": ["John", "Thabo", "Neo", "Jane", "John Doe"],
    "Love for Dogs (Magnitude)": [2.0, 4.6, -1.8, 12.7, 6.3],
    "Interview Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Dog Experiments", "Dog Ownership", "Weather Data"]
)

if data_option == "Dog Experiments":
    st.write("### Dog Experiment Data")
    st.dataframe(dog_data)
    # Add widget to filter by Dog Age (years)
    age_filter = st.slider("Filter by Dog Age (years)", 0.0, 10.0, (0.0, 10.0))
    filtered_dog = dog_data[
        dog_data["Dog Age (years)"].between(age_filter[0], age_filter[1])
    ]
    st.write(f"Filtered Results for Dog Age {age_filter}:")
    st.dataframe(filtered_dog)

elif data_option == "Dog Ownership":
    st.write("### Dog Ownership")
    st.dataframe(owner_data)
    # Add widget to filter by Love for Dogs
    love_filter = st.slider("Filter by Love for Dogs (Magnitude)", -2.0, 15.0, (-2.0, 15.0))
    filtered_dog = owner_data[
        owner_data["Love for Dogs (Magnitude)"].between(love_filter[0], love_filter[1])
    ]
    st.write(f"Filtered Results for Love Range {love_filter}:")
    st.dataframe(filtered_dog)

elif data_option == "Weather Data":
    st.write("### Weather Data")
    st.dataframe(weather_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_weather = weather_data[
        weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_weather)

# Add a contact section
st.header("Contact Information")
email = "napo.matsietsi@doggz.ac.za"
st.write(f"You can reach {name} at {email}.")




