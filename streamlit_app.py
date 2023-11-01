import streamlit as st

def main():

    # Read the HTML file into a string
    with open("hyd_builtup/hyd_builtup.html", "r") as f:
        html_string = f.read()

    # Display the HTML file in Streamlit
    st.components.html(html_string)

if __name__ == "__main__":
    main()
