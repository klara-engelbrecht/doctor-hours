import streamlit as st
import pandas as pd

# Set up the page
st.set_page_config(page_title="Multi-Section Adder", layout="wide")
st.title("📊 Multi-Section Sum Calculator")

# Initialize a dictionary to store all results
if 'results' not in st.session_state:
    st.session_state.results = {}

# Function to create a consistent input section
def create_section(section_name):
    st.subheader(f"{section_name} 🧮")
    
    col1, col2 = st.columns(2)
    with col1:
        x = st.number_input(f"x for {section_name}", value=0.0, step=1.0, key=f"x_{section_name}")
    with col2:
        y = st.number_input(f"y for {section_name}", value=0.0, step=1.0, key=f"y_{section_name}")
    
    # Calculate and display the section sum
    section_sum = x + y
    st.success(f"**{section_name} Subtotal: {x} + {y} = {section_sum}**")
    
    # Store the result in the session state
    st.session_state.results[section_name] = section_sum
    return section_sum

# Create 5 sections
sections = ["Revenue", "Expenses", "Assets", "Liabilities", "Investments"]
section_sums = {}

st.header("📋 Input Sections")
for section in sections:
    section_sums[section] = create_section(section)
    st.divider()  # Adds a visual separator between sections

# Calculate the grand total
grand_total = sum(st.session_state.results.values())

st.header("📈 Summary Results")

# Create a DataFrame for the results table
results_data = []
for section, subtotal in st.session_state.results.items():
    results_data.append({"Section": section, "Subtotal": subtotal})

# Add the grand total row
results_data.append({"Section": "**TOTAL**", "Subtotal": f"**{grand_total}**"})

results_df = pd.DataFrame(results_data)

# Display the table with some styling
st.dataframe(results_df, use_container_width=True, hide_index=True)

# Also display the grand total prominently
st.metric(label="🎯 Grand Total Across All Sections", value=grand_total)