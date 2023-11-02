import streamlit as st

path_to_html = "./hyd_builtup.html" 

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.components.v1.html(html_data,height=550)
