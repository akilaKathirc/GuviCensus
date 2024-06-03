import streamlit as st
import textract
from pathlib import Path

def textract_text_from_file(file_path):
    text = textract.process(file_path)
    return text.decode()

def CensusFileUpload():
    pageTitle = "Census Data Standardisation"
    pageIcon= ":money_with_wings:"
    layout = "centered"


    st.set_page_config(page_title=pageTitle, page_icon=pageIcon, layout=layout)
    st.title(pageTitle +"  "+pageIcon)





    st.title("Demo")
    # st.image(res, width = 800)

    st.markdown("**Please fill the below form :**")
    with st.form(key="Form :", clear_on_submit = True):
        Name = st.text_input("Name : ")
        Email = st.text_input("Email ID : ")
        UploadedFiles = st.file_uploader(label = "Upload file", type=["pdf","docx", "csv"],  accept_multiple_files=True)
        Submit = st.form_submit_button(label='Submit')
        

    st.subheader("Details : ")
    st.metric(label = "Name :", value = Name)
    st.metric(label = "Email ID :", value = Email)

    if Submit :
        st.markdown("**The file is sucessfully Uploaded.**")
        for uploaded_file in UploadedFiles:

        # Save uploaded file to './Data' folder.
            save_folder = './Data'
            save_path = Path(save_folder, uploaded_file.name)
            with open(save_path, mode='wb') as w:
                w.write(uploaded_file.getvalue())

            if save_path.exists():
                st.success(f'File {uploaded_file.name} is successfully saved!')

        





