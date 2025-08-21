import streamlit as st

st.title("Favorite Programming Languages Survey")

# Create individual checkboxes and store their state (True/False)
python = st.checkbox("Python")
javascript = st.checkbox("JavaScript")
java = st.checkbox("Java")
rust = st.checkbox("Rust")

# Button to submit the form
submitted = st.button("Submit Choices")

# Logic to run after the button is pressed
if submitted:
    selected_languages = []
    # Check which boxes are True and add them to the list
    if python:
        selected_languages.append("Python")
    if javascript:
        selected_languages.append("JavaScript")
    if java:
        selected_languages.append("Java")
    if rust:
        selected_languages.append("Rust")

    # Display the results
    if selected_languages:
        st.success(f"Your favorite languages are: **{', '.join(selected_languages)}**.")
    else:
        st.warning("You didn't select any languages!")