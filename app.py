import streamlit as st
import pandas as pd

# Title of the app
st.title("Dog Life & Benefits of Dog Walking")

st.image(
    "dog_03.jpg",
    caption="A happy dog is a happy man!"
)


st.text(
        "Research in the science of dog walking has been increasing throughout the years, where the benefits have been shown to far outway the negative consiquences. In this time of digital nomads, it is normal to sit for hours on a desk, focusing on the screen, while neglecting your your sorroundings as well as your dog.\nIt is in this light that this profile was created to detail the benefits of dog alking to the dogs, the dog owners and the community at large.\nThis profile will help showcase that trend and show how dog walking as a whole can help inprove the mood and happiness in communities.\n So what are you waiting for? Go out there, take your puppy with and get some Vitamin D."
        )


st.header("Dog Walking benefits")

# Second paragraphy
st.text(
        "Data for this profile was collected over a 10 year period which includes publications by this author on the subject matter")


# Collect basic information
name = "Dog Walker"
field = "Dog Sciences"
institution = "University of Doggz"


    

# Display basic profile information
st.subheader("Profile of the Author")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")


st.text(
        "Mr Walker who is a research fellow at the University of Doggz has been involved in the cognitive behaviour and well being of dogs and the relationships between dogs and their owners.\nHe has been featured on Paws Magazine, Canine Magazine and Animals.\nPrevious to his role at the Univerity of Doggz, he was a lecturer at the Malema Univerity where he ultimately became a dean. He has a strong passion for the sciences and has dedicated his life to the understanding of dogs and dog behaviour"
        )

# Generate dummy data
dog_data = pd.DataFrame({
    "Experiment": ["Labrador", "Pitbull", "German Sheperd", "Golden Retriver", "Poodle"],
    "Dog Age (years)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Barking Level": [1.3, 9.1, 3, 2, 12]
})

owner_data = pd.DataFrame({
    "Dog Owner": ["John", "Thabo", "Neo", "Jane", "John Doe"],
    "Love for Dogs (Magnitude)": [2.0, 4.6, -1.8, 12.7, 6.3],
    "Happiness level since survey": [5, 5.9, 4, 16, 19],
})


# Tabbed view for Dog Walking Data
st.subheader("Dog Walking Data")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Dog Experiments", "Dog Ownership"]
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


# Add a section for publications
st.subheader("Publications")

napo_csv = pd.read_csv("dog_walking_publications_index_v5_realistic_growth.csv")

uploaded_file = st.write(napo_csv)
#uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

# publications = (uploaded_file)
# st.write(publications)

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.column_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")


# Add a contact section
st.subheader("Contact Information")
email = "dog.walker@doggz.ac.za"
st.write(f"You can reach {name} at {email}.")

