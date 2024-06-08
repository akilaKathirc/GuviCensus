# import streamlit as st
# import pandas as pd
# import pyodbc
# from sqlQueries import sql_queries_dict

# # Function to convert complex types to native Python types
# def convert_to_native_type(val):
#     if isinstance(val, (list, tuple)):
#         return str(val)
#     if isinstance(val, dict):
#         return str(val)
#     if isinstance(val, (pd.Series, pd.DataFrame)):
#         return val.to_dict()
#     if isinstance(val, pyodbc.Row):  # Specific handling for pyodbc.Row
#         return tuple(val)
#     return val

# def runMsSQL():
#     selected_key = st.selectbox("Select a key:", list(sql_queries_dict.keys()))
#     query = sql_queries_dict.get(selected_key, 'default_value')
#     # Establish a connection to the MSSQL database
#     conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-3VBDJOUV;DATABASE=Census;UID=aki;PWD=aki'
#     conn = pyodbc.connect(conn_str)

#     # Execute the query using a cursor
#     cursor = conn.cursor()
#     cursor.execute(query)

#     # Fetch the data into a list of tuples
#     data = cursor.fetchall()

#     # Get column names from cursor description
#     columns = [col[0] for col in cursor.description]

#     # Convert the fetched data to a DataFrame
#     df = pd.DataFrame(data, columns=columns)

#     # Apply the conversion function to the DataFrame elements
#     for col in df.columns:
#         df[col] = df[col].apply(convert_to_native_type)

#     # Display the DataFrame using Streamlit
#     st.title('MSSQL Select Result with Data Conversion')
#     st.write('Original DataFrame:')
#     st.dataframe(df)


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


def runMsSQL():
    selected_key = st.selectbox("Select a key:", list(sql_queries_dict.keys()))
    query = sql_queries_dict.get(selected_key, 'default_value')
    st.write('SQL Query :',query)
    
# Establish a connection to the MSSQL database
    conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-3VBDJOUV;DATABASE=Census;UID=aki;PWD=aki'

    conn = pyodbc.connect(conn_str)

    # Define your SQL query
    # query = "SELECT * FROM your_table"

    # Execute the query using a cursor
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetch the data into a list of tuples
    data = cursor.fetchall()

    # Get column names from cursor description
    columns = [col[0] for col in cursor.description]
    data_list = [list(row) for row in data]

    # Convert the fetched data to a DataFrame
    df = pd.DataFrame(data_list, columns=columns)

    # Apply the conversion function to the DataFrame elements
    for col in df.columns:
        df[col] = df[col].apply(convert_to_native_type)

    # Display the DataFrame using Streamlit
    st.title('MSSQL Select Result with Data Conversion')
    st.dataframe(df)
