import streamlit as st
import pandas as pd

# Function to load data
@st.cache_data  # This will cache the data so it's not loaded every time the script runs
def load_data(file_path):
    return pd.read_csv(file_path, encoding='ISO-8859-1')

# Main function to run the app
def main():
    st.title('Email Lookup Dashboard')

    # File path to your CSV file
    file_path = 'total_file.csv'

    # Load data
    df = load_data(file_path)

    # Sidebar for user input
    st.sidebar.title('Enter ID Number')
    id_number = st.sidebar.text_input('Enter ID Number')

    # Display email if ID number is found
    if id_number:
        try:
            id_number = int(id_number)  # Convert input to integer if possible
            filtered_data = df[df['IDNUMBER'] == id_number]
            if not filtered_data.empty:
                email = filtered_data.iloc[0]['Email']
                st.write(f"Email address for ID {id_number}: {email}")
            else:
                st.warning(f"No email found for ID {id_number}")
        except ValueError:
            st.warning("Please enter a valid ID number")

if __name__ == '__main__':
    main()

