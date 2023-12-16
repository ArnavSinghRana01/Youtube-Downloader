import streamlit as st
import time as ts
from datetime import time
st.title("Form")
st.markdown("<h1> User Registration</h1", unsafe_allow_html=True)
# form = st.form("Form 1")
# form.text_input("First Name")
# form.form_submit_button("Submit")

with st.form("Form 2",clear_on_submit=True ):
    #creating column widget
    col1 ,col2 =st.columns(2)
    f_name=col1.text_input("First Name")
    l_name=col2.text_input("Last Name")
    #creating other inputs
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    
    day,month,year=st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state=st.form_submit_button("Submit")
    if s_state:
        if f_name=="" and l_name=="":
            st.warning("Please fill above fields")
        else:
            st.success("Submitted Successfully")
