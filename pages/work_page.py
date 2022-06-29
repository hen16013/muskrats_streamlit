# Run main_page.py first
import streamlit as st
import pandas as pd

# Set the page name
st.sidebar.markdown("# Worksheet Page")

# Load in data, and cache it so we don't have to load in a lot of data on refresh.
@st.cache
def get_data():
    return pd.read_csv("data.csv").drop(['_c0'],axis=1) #use different data here maybe
df = get_data()

# Write a header that says "Learning how to use Streamlit"

st.write("# Learning how to use streamlit!!")

# Create a check box labeled "Show data" that when checked, displays the dataframe

# def displayDataframe():
#     if st.session_state.isChecked == True:
#         st.write(df)

# st.checkbox("Show Data", on_change = displayDataframe(), key = "isChecked")

isChecked = st.checkbox("Show Data", value = True)

if isChecked:
    st.write(df)


# Create a slider that allows the user to choose a range between two years from our movie dataset

start_color, end_color = st.select_slider(
    'Select a range of color wavelength', value = (1970, 1980),
    # options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    min = 1970,
    max = 2005
    #  value=('red', 'blue')
    )
st.write('You selected years between', start_color, 'and', end_color)

