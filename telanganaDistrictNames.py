from pathlib import Path
from pyspark.sql.functions import col, when
import pandas as pd
from docxToArray import read_docx_to_dataframe
import streamlit as st


def open_file_with_pathlib(file_name):
   script_dir = Path(__file__).resolve().parent
   file_path = script_dir / file_name

   with open(file_path, 'r') as file:
      lines = [line.strip() for line in file.readlines()]
      return list(lines)

def updateTelanganaStateDistrictsNames():
    docx_path = "./Data/Telangana.docx"
    file_path = './Data/census_2011.csv'  # replace with the correct file path
    data = pd.read_csv(file_path)
    ct = read_docx_to_dataframe(docx_path)   #open_file_with_pathlib("Data\Telangana.txt")
    for distictName in ct:
        data.loc[data['District name'] == distictName, 'State name'] = 'Telangana'
    st.write("Telangana State Renamed districts:")
    st.dataframe(data[data['State name'] == 'Telangana'])




