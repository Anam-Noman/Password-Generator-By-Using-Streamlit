import streamlit as st
import string
import secrets

# Title
st.title("Password Generator")

# Header
st.header("Generate a strong password")

# Password length
password_length = st.number_input("Password length", min_value=8, max_value=128, value=12)

# Password options
options = st.multiselect("Select password options", ["Uppercase letters", "Lowercase letters", "Numbers", "Special characters"])

# Generate password function
def generate_password(length, options):
    characters = ""
    if "Uppercase letters" in options:
        characters += string.ascii_uppercase
    if "Lowercase letters" in options:
        characters += string.ascii_lowercase
    if "Numbers" in options:
        characters += string.digits
    if "Special characters" in options:
        characters += string.punctuation

    # Ensure that there are valid options for password generation
    if not characters:
        st.error("Please select at least one option for the password.")
        return None
    
    # Generate the password using secrets for cryptographically strong random values
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(password_length, options)
    if password:
        st.write(f"Generated Password: {password}")

        