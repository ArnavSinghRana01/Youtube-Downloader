import streamlit as st
import requests
from bs4 import BeautifulSoup

# Display a header using Markdown
st.markdown("<h1 style='text-align:center;'>WebScraper</h1>", unsafe_allow_html=True)

# Create a form for user input
with st.form("Search"):
    # Add a text input for the user to enter a keyword
    keyword = st.text_input("Enter Your Keyword")

    # Add a submit button for the form
    search = st.form_submit_button("Search")

    # Check if the form is submitted
    if search:
        # Send a request to the Unsplash website with the user's keyword
        page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
        # print(page.status_code)

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(page.content, 'html.parser')  # Use 'html.parser' instead of 'lxml' for this example

        # Print the entire HTML content for debugging
        print(soup.prettify())

        # Find all div elements with class "ripi6"
        rows = soup.findAll("div", class_="ripi6")
        # print(len(rows))

        # Loop through each row
        for row in rows:
            # Find all figure elements within the row
            figures = row.find_all("figure")

            # Loop through the first two figures
            for i in range(2):
                # Find the img element with class "YVj9w" within the figure
                img = figures[i].find("img", class_="YVj9w")

                # Print the img element for debugging
                print(img["srcset"].split("?"))
                print("\n\n")
