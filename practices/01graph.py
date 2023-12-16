import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

opt = st.sidebar.radio("Select any Graph", options=("Line", "Bar", "H-Bar"))

# Assuming x is defined somewhere in your code
x = np.linspace(0, 2 * np.pi, 100)
bar_x = np.array([1, 2, 3, 4, 5])  # Fix the array creation

if opt == "Line":
    st.markdown("<h1 style='text-align:center;'>Line Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    
    # Set the figure background color
    fig.patch.set_facecolor('#1f3557')  # Dark blue background color
    
    # Use the "seaborn-darkgrid" style
    plt.style.use("seaborn-darkgrid")
    
    # Get the current axes and set their background color
    ax = plt.gca()
    ax.set_facecolor('#1f3557')  # Dark blue background color
    
    # Plot the data with adjusted line colors
    plt.plot(x, np.sin(x), color='cyan')  # Adjust line color as needed
    plt.plot(x, np.cos(x), '--', color='magenta')  # Adjust line color as needed
    
    # Set the tick labels and axis labels to white
    ax.tick_params(axis='both', colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    
    st.pyplot(fig)
elif opt == "Bar":
    st.markdown("<h1 style='text-align:center;'>Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    
    # Set the figure background color
    fig.patch.set_facecolor('#1f3557')  # Dark blue background color
    
    # Use the "seaborn-darkgrid" style
    plt.style.use("seaborn-darkgrid")
    
    ax = plt.gca()
    ax.set_facecolor('#1f3557')  # Dark blue background color
    
    plt.bar(bar_x, bar_x * 10, color='skyblue')  # Adjust bar color as needed
    
    # Set the tick labels and axis labels to white for Bar Chart
    ax.tick_params(axis='both', colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    
    st.pyplot(fig)
else:
    st.markdown("<h1 style='text-align:center;'>Horizontal Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    
    # Set the figure background color
    fig.patch.set_facecolor('#1f3557')  # Dark blue background color
    
    # Use the "seaborn-darkgrid" style
    plt.style.use("seaborn-darkgrid")
    
    ax = plt.gca()
    ax.set_facecolor('#1f3557')  # Dark blue background color
    
    plt.barh(bar_x * 10, bar_x, color='lightcoral')  # Adjust bar color as needed
    
    # Set the tick labels and axis labels to white for Horizontal Bar Chart
    ax.tick_params(axis='both', colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    
    st.pyplot(fig)
