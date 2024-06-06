import sqlite3
import streamlit as st
import pandas as pd

# Create a connection to the SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('DeepDermaDatabase.db')

# Function to create the database and table
def create_database():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS deep_derma (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disease TEXT NOT NULL,
            causes TEXT NOT NULL,
            symptoms TEXT NOT NULL,
            treatment_suggestions TEXT NOT NULL
        )
    ''')
    conn.commit()

# Function to add a new record to the database
def add_record(disease, causes, symptoms, treatment_suggestions):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO deep_derma (disease, causes, symptoms, treatment_suggestions)
        VALUES (?, ?, ?, ?)
    ''', (disease, causes, symptoms, treatment_suggestions))
    conn.commit()

# Function to get all records from the database
def get_all_records():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM deep_derma')
    rows = cursor.fetchall()
    return rows

# Create the database and table
create_database()

# Streamlit app layout
st.title("Deep Derma Database")

# Form to add a new record
with st.form("record_form"):
    st.header("Add New Record")
    disease = st.text_input("Disease")
    causes = st.text_area("Causes")
    symptoms = st.text_area("Symptoms")
    treatment_suggestions = st.text_area("Treatment Suggestions")
    submitted = st.form_submit_button("Add Record")
    if submitted:
        add_record(disease, causes, symptoms, treatment_suggestions)
        st.success("Record added to the database")

# Display all records in the database
st.header("All Records")
records = get_all_records()
df = pd.DataFrame(records, columns=["ID", "Disease", "Causes", "Symptoms", "Treatment Suggestions"])
st.dataframe(df)
