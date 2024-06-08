import pandas as pd
from sqlalchemy import create_engine
import streamlit as st
from sqlQueries import sql_queries_dict
import pyodbc
import pyarrow as pa



# Define a function to convert complex types to native Python types
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


def runSqlScript1(query):
    mssql_conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=LAPTOP-3VBDJOUV;'
        'DATABASE=Census;'
        'UID=aki;'
        'PWD=aki'
    )
    mssql_cursor = mssql_conn.cursor()
    df=pd.DataFrame(mssql_cursor.execute(query))
    df = df.applymap(convert_to_native_type)
    try:
        table = pa.Table.from_pandas(df, preserve_index=False)
        st.dataframe(table)
        print("Serialization successful!")
    except Exception as e:
        print(f"Serialization failed: {e}")
    


def runSqlScript2(query):
    
     # MSSQL connection parameters
    server = 'LAPTOP-3VBDJOUV'
    database = 'Census'
    username = 'aki'
    password = 'aki'
    table_name = "census_2011"
    # Create connection string
    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

    # Create a connection to the MSSQL database
    engine = create_engine(connection_string)
    return pd.DataFrame(pd.read_sql_query(query, engine))

def runSqlQuery(query):
    server = 'LAPTOP-3VBDJOUV'
    database = 'Census'
    username = 'aki'
    password = 'aki'
    table_name = "census_2011"
    # Create connection string
    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
   
    # Create an engine
    engine = create_engine(connection_string)

    # Use pandas to execute the query and return a DataFrame
    return pd.read_sql_query(query, engine)


def SQLFinalOutput():
    # Title of the app
    st.title("SQL select Output")

    # Dropdown menu populated with dictionary keys
    selected_key = st.selectbox("Select a key:", list(sql_queries_dict.keys()))
    # selected_val = st.selectbox("Select a key:", list(sql_queries_dict.values()))
    selected_val = sql_queries_dict.get(selected_key, 'default_value')


    # Submit button
    if st.button("Submit"):
        st.write("Selected Query Name:", selected_key)
        st.write("Sql Query executed:", selected_val)
        st.write("Output:")
        runSqlScript1(selected_val)



