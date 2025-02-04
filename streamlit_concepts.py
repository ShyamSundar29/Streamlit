import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Basic Concepts


# Display a title
st.title("Hello, Shyam!")

# Display different text sizes
# st.header("Wlecome to Streamlit!")
# st.subheader("First Streamlit App")

# # Display simple text
# st.text("you are made this app.")

# Displaying Data:


# Create a simple dataframe
st.header("Welcome here is your DataFrame!")
df = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Shyam", "David", "Paul"]})
# Display dataframe in Streamlit
st.dataframe(df)
# Save to CSV file
df.to_csv("data.csv", index=False)

# Widgets (User Input):

# User input widgets
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0)
agree = st.checkbox("I agree")



# Intermediate Features

# Layout Customization

# Sidebar:
# Create a sidebar
st.sidebar.header("Sidebar")
# Sidebar selection box
option = st.sidebar.selectbox("Choose a number", [1, 2, 3])

#slider
age = st.slider("Select your age:", min_value=0, max_value=100)
st.write("You selected:", age)

# Columns:

# Create two columns
col1, col2 = st.columns(2)
# Add content to columns
col1.write("This is column 1")
col2.write("This is column 2")


# Expander:

# Create an expander for additional info
with st.expander("More Info"):
    st.write("This is additional information.")


# Displaying Charts

# Matplotlib Chart:
# Create a simple line plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

# Display the plot in Streamlit
st.pyplot(fig)

# Advanced Topics

# Caching for Performance Optimization
# Use @st.cache_data for caching data and @st.cache_resource for caching external objects like models:

@st.cache_data  # Cache the function output to optimize performance
def load_data():
    return pd.read_csv("data.csv")

data = load_data()
st.dataframe(data)

# Session State Management

# Maintain state across reruns using st.session_state:
# Initialize session state variable
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Increment counter on button click
if st.button("Increment"):
    st.session_state.counter += 1

# Display counter value
st.write("Counter:", st.session_state.counter)


#Selectbox
options = ["Python", "Java", "C++"]
choice = st.selectbox("Choose a programming language", options)
st.write("You selected:", choice)

#upload file
uploaded_file = st.file_uploader("Choose a file",type=['csv',"docx","txt","pdf"])
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    df = pd.read_csv(uploaded_file)
    st.write(df)

# Running a Streamlit App
# streamlit run streamlit_concepts.py