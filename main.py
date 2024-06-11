import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Set page configuration
st.set_page_config(page_title="Executive Summary Dashboard", layout="wide")

# Title and tabs
st.title("Executive Summary")
tabs = ["Descriptive", "Diagnostics", "Predictive & Prescriptive"]
selected_tab = st.selectbox("Select a tab", tabs)

# Sub-tabs for Descriptive tab
if selected_tab == "Descriptive":
    sub_tabs = ["Executive Summary", "Category Summary", "Regional Summary"]
    selected_sub_tab = st.selectbox("Select a sub-tab", sub_tabs)

    if selected_sub_tab == "Executive Summary":
        st.header("Executive Summary")
        st.markdown("### Key Metrics")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Sell out Volume", "423K", "24% YOY")
        col2.metric("Sell out Value", "R$57.168K", "38% YOY")
        col3.metric("Sell out Units", "4.536K", "4% YOY")
        col4.metric("Avg Price Per Unit", "R$12.60", "32% YOY")
        
        col1.metric("Sell out Volume (Own Brand)", "259K", "5% YOY")
        col2.metric("Sell out Value (Own Brand)", "R$36.072K", "19% YOY")
        col3.metric("Sell out Units (Own Brand)", "3.442K", "-2% YOY")
        col4.metric("Avg Price Per Unit (Own Brand)", "R$10.48", "10% YOY")
        
        # Charts
        st.markdown("### Volume Market Share")
        volume_market_share_data = pd.DataFrame({
            'Month': pd.date_range(start='1/1/2022', periods=12, freq='M'),
            'Manufacturer 1': np.random.rand(12) * 4 + 2,
            'Manufacturer 2': np.random.rand(12) * 3 + 1,
            'Manufacturer 3': np.random.rand(12) * 2
        })
        st.line_chart(volume_market_share_data.set_index('Month'))
        
        st.markdown("### Value Sales - Quarter Analysis")
        quarter_analysis_data = pd.DataFrame({
            'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
            'Manufacturer 1': [5000000, 10000000, 15000000, 20000000],
            'Manufacturer 2': [3000000, 7000000, 11000000, 15000000],
            'Manufacturer 3': [2000000, 4000000, 6000000, 8000000]
        })
        st.bar_chart(quarter_analysis_data.set_index('Quarter'))
        
        st.markdown("### Value Sales - Region wise")
        region_data = pd.DataFrame({
            'Region': ['AREA 1', 'AREA 2', 'AREA 3'],
            'Value': [41, 29, 30]
        })
        region_pie_chart = alt.Chart(region_data).mark_arc().encode(
            theta=alt.Theta(field="Value", type="quantitative"),
            color=alt.Color(field="Region", type="nominal"),
            tooltip=['Region', 'Value']
        )
        st.altair_chart(region_pie_chart, use_container_width=True)
        
        st.markdown("### Value Sales - Channel wise")
        channel_data = pd.DataFrame({
            'Channel': ['ECom', 'GT', 'MT'],
            'Value': [18, 24, 58]
        })
        channel_pie_chart = alt.Chart(channel_data).mark_arc().encode(
            theta=alt.Theta(field="Value", type="quantitative"),
            color=alt.Color(field="Channel", type="nominal"),
            tooltip=['Channel', 'Value']
        )
        st.altair_chart(channel_pie_chart, use_container_width=True)
        
        st.markdown("### Value Sales - Performance over time")
        performance_data = pd.DataFrame({
            'Month': pd.date_range(start='1/1/2022', periods=12, freq='M'),
            'Manufacturer 1': np.random.rand(12) * 4 + 2,
            'Manufacturer 2': np.random.rand(12) * 3 + 1,
            'Manufacturer 3': np.random.rand(12) * 2
        })
        st.line_chart(performance_data.set_index('Month'))

# Filters
st.sidebar.header("Filters")
st.sidebar.selectbox("Year", [2022, 2023])
st.sidebar.selectbox("Quarter", ["All", "Q1", "Q2", "Q3", "Q4"])
st.sidebar.selectbox("Month", ["All", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
st.sidebar.selectbox("Country", ["All", "Country 1", "Country 2", "Country 3"])
st.sidebar.selectbox("Region", ["All", "Region 1", "Region 2", "Region 3"])
st.sidebar.selectbox("Channel", ["All", "Channel 1", "Channel 2", "Channel 3"])
st.sidebar.selectbox("Manufacturer", ["All", "Manufacturer 1", "Manufacturer 2", "Manufacturer 3"])
st.sidebar.selectbox("Division", ["All", "Division 1", "Division 2", "Division 3"])
st.sidebar.selectbox("Brand", ["All", "Brand 1", "Brand 2", "Brand 3"])
st.sidebar.selectbox("Product", ["All", "Product 1", "Product 2", "Product 3"])
st.sidebar.selectbox("KPI", ["All", "KPI 1", "KPI 2", "KPI 3"])
