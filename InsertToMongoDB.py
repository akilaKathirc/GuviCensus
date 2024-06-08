import os

import streamlit as st
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv


load_dotenv(".env")
client=MongoClient(os.getenv("MongoClient"))

db=client.GuviCensusData
collection=db.CensusData_2011

def insert_censusdata_2011(df):
    st.dataframe(df)
    # Convert DataFrame to dictionary format and insert into MongoDB
    collection.insert_many(df.to_dict('records'))


def fetch_all_periods():
    return collection.find()
