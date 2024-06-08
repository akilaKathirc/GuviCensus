import streamlit as st

from FileUpload import CensusFileUpload
from FinalOp import SQLFinalOutput
from FinalOutPut import runSqlScript
from FixNullValues import FixNullValues
from MongoToMsSql import MongoToSqlServer
from renameColumn import renameCensusDataFile
from telanganaDistrictNames import updateTelanganaStateDistrictsNames

# Define different pages as functions
def home():
    st.title("Home")
    st.write("Welcome to the home page!")
    if st.button("Go to FileUpload"):
        st.session_state.page = 'FileUpload'
        st.rerun()

def FileUpload():
    CensusFileUpload()
    if st.button("ColumnRenaming"):
        st.session_state.page = 'rename1'
        st.rerun()
    
def rename():
    renameCensusDataFile()
    if st.button("Telengana Districts Name  change"):
        st.session_state.page = 'TelenganaDt'
        st.rerun()

def telenganaDt():
    st.title("Telangana District Names Changed as below")
    updateTelanganaStateDistrictsNames()
    if st.button("Clean and Fix Null Values"):
        st.session_state.page = 'CleanandFix'
        st.rerun()


def contact():
    st.title("Contact")
    st.write("This is the contact page.")
    if st.button("Go to FileUpload"):
        st.session_state.page = 'FileUpload'
        st.rerun()
    if st.button("Go to Home"):
        st.session_state.page = 'home'
        st.rerun()

def FixNullValue():
    FixNullValues()
    st.write("Data pushed to Mongo DB")
    if st.button("Mongo To MsSql"):
        st.session_state.page = 'mongoToSql'
        st.rerun()

def MongoToMsSql():
    MongoToSqlServer()
    if st.button("Sql Selects"):
        st.session_state.page = 'SqlSelects'
        st.rerun()
    
def SqlSelectQueryOutput():
    # SQLFinalOutput()
    runSqlScript()

# Initialize session state for page if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Routing logic
if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'FileUpload':
    FileUpload()
elif st.session_state.page == 'TelenganaDt':
    telenganaDt()
elif st.session_state.page == 'rename1':
    rename()
elif st.session_state.page == 'CleanandFix':
    FixNullValue()
elif st.session_state.page == 'mongoToSql':
    MongoToMsSql()
elif st.session_state.page == 'SqlSelects':
    SqlSelectQueryOutput()

    
    
