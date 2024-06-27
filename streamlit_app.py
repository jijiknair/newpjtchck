import pandas as pd
import streamlit as st

# Function to load data
@st.cache
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except pd.errors.ParserError as e:
        st.error(f"Error parsing CSV file: {str(e)}")
        return None
    except Exception as e:
        st.error(f"Error loading CSV file: {str(e)}")
        return None

# Function to display email lookup dashboard
def main():
    file_path = 'https://github.com/jijiknair/newpjtchck/blob/master/TOTALfile.csv'
    df = load_data(file_path)

    if df is not None:
        st.write(df.head())  # Display first few rows to verify data

        # Example: Email lookup based on IDNUMBER
        id_number = '12345'
        if 'IDNUMBER' in df.columns:
            email = df[df['IDNUMBER'] == id_number]['Email'].values
            st.write(f"Email found: {email}")
        else:
            st.warning("IDNUMBER column not found in the CSV file.")

if __name__ == "__main__":
    main()
