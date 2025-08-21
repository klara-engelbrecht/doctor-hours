import streamlit as st

# Set up the page
st.set_page_config(page_title="Simple Adder", layout="centered")
st.title("➕ Simple Addition App")

# Using st.number_input for numerical input
st.header("Enter Two Numbers")
x = st.number_input("Select the first number (x)", value=0.0, step=0.1)
y = st.number_input("Select the second number (y)", value=0.0, step=0.1)

# Calculate the sum
result = x + y

# Display the result
st.header("Result")
st.success(f"**{x} + {y} = {result}**")

# Optional: Add some explanation
st.divider()
st.markdown("""
**How it works:**
1. Use the number inputs above to choose values for `x` and `y`.
2. The app automatically calculates the sum in real-time.
3. No submit button needed – Streamlit updates instantly! ⚡
""")