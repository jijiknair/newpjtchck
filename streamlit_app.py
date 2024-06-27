import streamlit as st
import pandas as pd

@st.cache
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, error_bad_lines=False)
        return df
    except Exception as e:
        st.error(f"Error loading CSV file: {str(e)}")
        return None

def main():
    st.title('Email Lookup Dashboard(منصة لإيجاد بريدك الالكتروني)')

    # Sidebar for user input (id number)
    st.sidebar.title('Input ID Number(رقم البطاقة الشخصية  (الرقم المدني))')
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
