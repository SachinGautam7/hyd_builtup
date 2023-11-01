import streamlit as st
import io

def read_html_file(filename):
  with io.open(filename, "r", encoding="utf-8") as f:
    html = f.read()
  return html

html = read_html_file("hyd_builtup/hyd_builtup.html")

st.components.html(html)
