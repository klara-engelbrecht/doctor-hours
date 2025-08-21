import streamlit as st
import pandas as pd

# Set up the page
st.set_page_config(page_title="Multi-Section Adder", layout="wide")
st.title("🧮 Overtime calculator")

# Initialize a dictionary to store all results
if 'results' not in st.session_state:
    st.session_state.results = {}

# Function to create a consistent input section
def create_section(section_name):
    st.subheader(f"{section_name}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        x = st.number_input(f"x for {section_name}", value=0.0, step=1.0, key=f"x_{section_name}")
    with col2:
        y = st.number_input(f"y for {section_name}", value=0.0, step=1.0, key=f"y_{section_name}")
    with col3:
        y = st.number_input(f"z for {section_name}", value=0.0, step=1.0, key=f"z_{section_name}")
    with col4:
        y = st.number_input(f"w for {section_name}", value=0.0, step=1.0, key=f"w_{section_name}")
    
    # Calculate and display the section sum
    section_sum = x + y
    st.success(f"**{section_name} hours: {section_sum}**")
    
    # Store the result in the session state
    st.session_state.results[section_name] = section_sum
    return section_sum

# Create 5 sections
sections = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
section_sums = {}

# st.header("📋 Input Section")
for section in sections:
    section_sums[section] = create_section(section)
    st.divider()  # Adds a visual separator between sections

# Calculate the grand total
grand_total = sum(st.session_state.results.values())

st.header("📈 Weekly hours")

# Create a DataFrame for the results table
results_data = []
for section, subtotal in st.session_state.results.items():
    results_data.append({"Weeks": section, "Hours": subtotal})

# Add the grand total row
results_data.append({"Section": "Month's hours", "Subtotal": f"**{grand_total}**"})

results_df = pd.DataFrame(results_data)

# Display the table with some styling
st.dataframe(results_df, use_container_width=True, hide_index=True)

# Also display the grand total prominently
st.metric(label="📈 Total hours for the month", value=grand_total)