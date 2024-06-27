import streamlit as st
import pandas as pd



def main():
# Load the CSV file into a DataFrame with specified encoding
@st.cache_data
def load_data(file_path, encoding='utf-8'):
    return pd.read_csv(file_path, encoding=encoding)

def get_email_by_id(df, user_id):
    result = df[df['IDNUMBER'] == user_id]
    if not result.empty:
        return result.iloc[0]['Email']
    else:
        return None

# Load data
file_path = r'C:\Users\DELL\OneDrive\Desktop\pjt\TOTALfile.csv'  # Use raw string literal here
encoding = 'ISO-8859-1'  # or 'utf-16' or any other appropriate encoding
df = load_data(file_path, encoding)

# Streamlit app
st.title('Email Lookup Dashboard')
if __name__ == '__main__':
    main()

# Input field for user ID
user_id = st.number_input('Enter User ID', min_value=1, step=1)

# Button to fetch email
if st.button('Get Email'):
    email = get_email_by_id(df, user_id)
    if email:
        st.success(f'The email address for user ID {user_id} is {email}.')
    else:
        st.error(f'No email address found for user ID {user_id}.')
