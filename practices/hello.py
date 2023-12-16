import streamlit as st 
import pandas as pd
#creating data frame
table = pd.DataFrame({"Column 1":[1,2,3,4,5,6,7],"Column2":[11,12,13,14,15,16,17]})
#add title
st.title("Welcome")
#header
st.header("Body")
#sub header
st.subheader("Hey")

st.text("Hi , Welcome to the Page")
#MArkdown display formatted text, headers, links, lists, and other
st.markdown("---") #horizontal line
st.markdown("[Google](https://www.google.com)")#Add links

#adding captions
st.markdown("---")
st.caption("Hi , I am caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}") #you can use latex to import any mathamatical function
#adding json quote
json = {"a":"1,2,3","b":"4,5,6"}
st.json(json)
#adding code
code = """
a = 1
b = 2
print(a+b)
"""
st.code(code, language="python")

st.write("## H2")

st.metric(label="Wind Speed", value="120ms⁻¹", delta = "-1.4ms⁻¹")
#delta is use if there is any value changing    
#Creating table 
st.table(table)
st.dataframe(table) #creating df