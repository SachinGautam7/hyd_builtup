import streamlit as st
import io
import json

def read_html_file(filename):
  with io.open(filename, "r", encoding="utf-8") as f:
    html = f.read()
  return html

html = read_html_file("./hyd_builtup.html")

# Render the HTML file in a hidden iframe
iframe_html = """
<iframe id="fullscreen-iframe" style="display: none;"></iframe>
"""

st.components.html(iframe_html)

# Expand the iframe to fullscreen using JavaScript
js_code = """
document.getElementById("fullscreen-iframe").style.display = "block";
document.getElementById("fullscreen-iframe").requestFullscreen();
"""

st.components.v1.html(js_code, height=0, width=0)
