import streamlit as st
import time as ts
from datetime import time
st.title("Uploading File")
st.markdown("---")

def converter(value):
    m,s,mm = value.split(":")
    t_s = int(m)*60+int(s)+int(mm)/1000
    return t_s
    
#uploading files
images =st.file_uploader("Please upload an image", type=["png","jpg","jpeg"], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)
        
#create sliders
# val =st.slider("This is a slider", min_value=40,max_value=100, value=70)
# print(val)
#text inputs 
# val =st.text_input("Enter your course title.", max_chars=60)
# val = st.text_area("Course decription", max_chars=500)
# print(val)
#date and time input
# val = st.date_input("Enter your registration date")
val = st.time_input("Set Timer", value=time(0,0,0)) #setting default value with 00
if str(val) == "00:00:00":
    st.write("Please set timer")
else:
    sec =converter(str(val))
    print(sec)
    #Progress bar
    bar=st.progress(0)
    per=sec/100
    progress_statue = st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_statue.write(str(i+1)+ "%")
        ts.sleep(per)
    
    


















#set image
# st.image("34297.jpg", caption = "Iron Man", width =680)
# #Importing Audio
# st.audio("harleys-In-Hawaii.mp3")
# #importing video
# st.video("nav1.mp4")

# def change():
#     print(st.session_state.checker)
# state = st.checkbox("Checkbox", value=True, on_change = change, key ="checker") #creat checkbox
# #RADIO BUttons 
# radio_btn = st.radio("In which country do you live ?", options=("US","UK","INDIA"))
# print(radio_btn)

# def btn_click():
#     print("Button clicked")
# btn=st.button("Click Me", on_click=btn_click)
# #select box/multiple boxes
# select=st.selectbox("What is your favorite car?",options=("Please Select","Audi","BMW","Ferrari","Skoda"))
# print(select)

# multi_select =st.multiselect("What is your favorite color?", options=("Blue","Black","Pink","Grey"))
# st.write(multi_select)
