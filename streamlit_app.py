import streamlit as st

from streamlit_js_eval import streamlit_js_eval

st.write(f"Screen width is {streamlit_js_eval(js_expressions='screen.width', key = 'SCR')}")
st.write(f"Screen height is {streamlit_js_eval(js_expressions='screen.height', key = 'SCR1')}")

# path_to_html = "./hyd_builtup.html" 

# # Read file and keep in variable
# with open(path_to_html,'r') as f: 
#     html_data = f.read()

# st.set_page_config(layout='wide')
# ## Show in webpage
# st.components.v1.html(html_data, height=)
