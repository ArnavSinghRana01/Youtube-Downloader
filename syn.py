import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv("synthetic_financial_data.csv")

# Set page title and icon
st.set_page_config(page_title="Financial Transaction Analysis", page_icon=":chart_with_upwards_trend:", layout="wide")
st.title(":chart_with_upwards_trend: Synthetic Financial Data Visualization")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Display dataset
st.subheader("Financial Transaction Data")
st.dataframe(data)

# Filter options
st.sidebar.header("Filter Options")

# Filter by Fraudulent transactions
fraudulent_transactions = st.sidebar.checkbox("Show Fraudulent Transactions", value=True)
if not fraudulent_transactions:
    data = data[data['is_fraudulent'] == 0]

# Filter by Card Type
selected_card_type = st.sidebar.selectbox("Select Card Type", data['card_type'].unique())
if selected_card_type != "All":
    data = data[data['card_type'] == selected_card_type]

# Summary Statistics
st.sidebar.header("Summary Statistics")
st.sidebar.write("Total Transactions:", data.shape[0])
st.sidebar.write("Total Amount:", data['amount'].sum())
st.sidebar.write("Total Fraudulent Transactions:", data[data['is_fraudulent'] == 1].shape[0])

# Visualizations
st.header("Data Visualizations")

# Pie chart for Fraudulent Transactions
fig_pie = px.pie(data, names='is_fraudulent', title='Fraudulent Transactions Distribution')
fig_pie.update_layout(margin=dict(l=10, r=10, b=10, t=50), showlegend=False)
st.plotly_chart(fig_pie)



# Scatter plot for Amount vs. Customer Age
fig_scatter = px.scatter(data, x='amount', y='customer_age', color='is_fraudulent',
                         title='Scatter Plot: Amount vs. Customer Age')
fig_scatter.update_layout(margin=dict(l=10, r=10, b=10, t=50), showlegend=False)
st.plotly_chart(fig_scatter)
