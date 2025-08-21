import streamlit as st

st.title("➕ Addition App with Submit Button")

x = st.number_input("Select the first number (x)", value=0.0, step=0.1)
y = st.number_input("Select the second number (y)", value=0.0, step=0.1)

# Create a button. Only calculate when it's clicked.
calculate = st.button("Calculate Sum")

if calculate:
    result = x + y
    st.success(f"**{x} + {y} = {result}**")
else:
    st.info("👆 Enter your numbers and press the button to calculate!")