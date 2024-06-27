import streamlit as st
import pandas as pd

# Load data (assuming you have a CSV with 'id' and 'email' columns)
@st.cache  # Cache the data to speed up app performance
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def main():
    st.title('Email Lookup Dashboard')

    # Sidebar for user input (id number)
    st.sidebar.title('Input ID Number')
    id_number = st.sidebar.number_input('Enter ID Number', min_value=1, step=1)

    # Load data
    file_path = 'https://github.com/jijiknair/newpjtchck/blob/master/TOTALfile.csv'
    df = load_data(file_path)

    # Lookup email based on id number
    email = df[df['IDNUMBER'] == id_number]['Email'].values
    if len(email) > 0:
        st.write(f"Email found: {email[0]}")
    else:
        st.write("Email not found for this ID.")

if __name__ == '__main__':
    main()
