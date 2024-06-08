import streamlit as st
import pandas as pd
import pyodbc
from sqlQueries import sql_queries_dict

# Function to convert complex types to native Python types
def convert_to_native_type(val):
    if isinstance(val, (list, tuple)):
        return str(val)
    if isinstance(val, dict):
        return str(val)
    if isinstance(val, (pd.Series, pd.DataFrame)):
        return val.to_dict()
    if isinstance(val, pyodbc.Row):  # Specific handling for pyodbc.Row
        return tuple(val)
    return val

def runSqlScript():
    mssql_conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=LAPTOP-3VBDJOUV;'
        'DATABASE=Census;'
        'UID=aki;'
        'PWD=aki'
    )
    
    # Define your SQL query
    # query = "SELECT * FROM your_table"
    selected_key = st.selectbox("Select a key:", list(sql_queries_dict.keys()))
    # selected_val = st.selectbox("Select a key:", list(sql_queries_dict.values()))
    query = sql_queries_dict.get(selected_key, 'default_value')
    st.write("Sql Query executed:", query)

    # Execute the query using a cursor
    cursor = mssql_conn.cursor()
    cursor.execute(query)

    # Fetch the data into a DataFrame
    data = cursor.fetchall()
    # df = pd.DataFrame(data, columns=[col[0] for col in cursor.description])
    df = pd.DataFrame(data)

    # Apply the conversion function to the DataFrame elements
    # for col in df.columns:
        # df[col] = df[col].apply(convert_to_native_type)
    # df = df.map(convert_to_native_type)
    # Display the DataFrame using Streamlit
    st.title('MSSQL Select Result with Data Conversion')
    st.write('Original DataFrame:')
    st.dataframe(df)
    st.title("SQL select Output")
    mssql_conn.commit()
    cursor.close()
    mssql_conn.close()

    
