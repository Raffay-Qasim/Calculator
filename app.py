import streamlit as st

# Function to perform the basic operations
def calculate(operation, num1, num2):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero"

# Streamlit interface
st.title("Simple Streamlit Calculator")

# Taking user input
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Dropdown menu for selecting operation
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the calculation when button is pressed
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"The result of {operation}ing {num1} and {num2} is: {result}")
