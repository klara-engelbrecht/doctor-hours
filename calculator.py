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
        x = st.number_input(f"Hours for {section_name} - Day 1", value=0.0, step=1.0, key=f"x_{section_name}")
    with col2:
        y = st.number_input(f"Hours for {section_name} - Day 2", value=0.0, step=1.0, key=f"y_{section_name}")
    with col3:
        z = st.number_input(f"Hours for {section_name} - Day 3", value=0.0, step=1.0, key=f"z_{section_name}")
    with col4:
        w = st.number_input(f"Hours for {section_name} - Day 4", value=0.0, step=1.0, key=f"w_{section_name}")
    
    # Calculate and display the section sum (now including all 4 variables)
    section_sum = x + y + z + w
    st.success(f"**{section_name} total hours: {section_sum}**")
    
    # Store the result in the session state
    st.session_state.results[section_name] = section_sum
    return section_sum

# Create 5 sections
sections = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
section_sums = {}

for section in sections:
    section_sums[section] = create_section(section)
    st.divider()  # Adds a visual separator between sections

# Calculate the grand total
grand_total = sum(st.session_state.results.values())

st.header("📈 Weekly hours")

# Create a DataFrame for the results table (without the total row)
results_data = []
for section, subtotal in st.session_state.results.items():
    results_data.append({"Week": section, "Hours": subtotal})

results_df = pd.DataFrame(results_data)

# Display the table with some styling
st.dataframe(results_df, use_container_width=True, hide_index=True)

# Display the total prominently below the table as a metric
st.metric(label="📊 Total hours for the month", value=grand_total)

# Optional: Also display the total as bold text using markdown
st.markdown(f"**📅 Month's total hours: {grand_total}**")