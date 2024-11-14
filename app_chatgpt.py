import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import os
import streamlit as st

warnings.filterwarnings('ignore')
import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.simpson-associates.co.uk/wp-content/uploads/2018/02/bg2.jpg");
        background-size:cover
    }

    </style>
    """,
    unsafe_allow_html=True
)


# Define custom CSS styles for enhanced UI
st.markdown("""
    <style>
        /* Global Background */
        body {
            background-color: blue /* Light pink gradient */
            font-family: 'monospace', sans-serif;
        }

        /* Header Styling */
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            background-color: white; /* Green */
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .logo {
            width: 100px; /* Set logo size */
        }
        .guidance-text {
            font-size: 16px;
            font-weight: bold;
            color: #ffffff; /* White text */
            text-align: center;
        }
        /* Title Styling */
        .main-title {
            font-size: 30px; /* Reduced font size */
            font-weight: bold;
            text-align: center;
            color: white; /* White text */
            background-color:#AEC6CF; /* Indigo */
            padding: 5px;
            border-radius: 10px;
            margin-bottom: 20px;
            width:450px
        }
        /* Sidebar Styling */
        .sidebar-title {
            font-weight: bold;
            font-size: 20px;
            color: red ; /* Indigo */
            text-align: center;
            margin-bottom: 10px;
        }
        .sidebar {
            background-color: blue; /* Light background for sidebar */
        }

        /* Footer Section */
        .footer {
            font-size: 18px;
            text-align: center;
            padding: 10px;
            color: #888;
            margin-top: 20px;
            border-top: 1px solid #ccc;
            background-color: white; /* Green footer */
            color: blue; /* White text */
        }
    </style>
""", unsafe_allow_html=True)

# Header Section with Scrolling Guidance Text
scrolling_text = """
    <marquee behavior="scroll" direction="left">
        <span style="font-weight: bold; font-size: 24px; color: white;">UNDER THE GUIDANCE OF OMKAR NALLAGONI SIR</span>
    </marquee>
"""
st.markdown(scrolling_text, unsafe_allow_html=True)

# Main Title and Description
st.markdown('<div class="main-title">EXPLORATORY DATA ANALYSIS</div>', unsafe_allow_html=True)
import streamlit as st

# Custom CSS for styling text color
st.markdown(
    """
    <style>
    .custom-text {
        color:white; /* Change to your preferred color (e.g., Tomato color) */
        font-weight:bold;
        font-size:18px;
    }
    .custom-text2{
        color:white; /* Change to your preferred color (e.g., Tomato color) */
        font-weight:bold;
        font-size:60px;

    }
    .custom-text3{
        color:white; /* Change to your preferred color (e.g., Tomato color) */
        font-weight:bold;
        font-size:20px;
        background-color:grey;
        width:200px
    }
    </style>

    """,
    unsafe_allow_html=True
)

# Applying custom style to your content
st.write("""
<div class="custom-text">
About Exploratory Data Analysis (EDA)
EDA is a critical step in data science that involves analyzing datasets to summarize their main characteristics. Through visualizations, 
descriptive statistics, and outlier analysis, EDA helps uncover patterns, detect anomalies, and form hypotheses. This app enables users to perform EDA 
with various plot options, such as bar charts, pie charts, histograms, and box plots, and also provides a correlation heatmap and crosstab analysis.
</div>
<div>
<div class="custom-text3">
How to Use the App
</div>
<ol class="custom-text2">
<li>Upload your dataset (CSV or Excel).</li>
<li>Choose a visualization type from the sidebar.</li>
<li>Customize your plot settings and hit 'Submit' to generate the visualization.</li>
<li>Analyze the output and make informed decisions based on the insights gathered.</li>
</ol>
""", unsafe_allow_html=True)


# Sidebar for Plot Selection
st.sidebar.markdown('<div class="sidebar-title">Different Plots</div>', unsafe_allow_html=True)
st.sidebar.write("Select plot and charts")
file = st.file_uploader('Choose a file', type=['csv', 'xlsx'], help="Upload a .csv or .xlsx file")

# Footer Section
#st.markdown('<div class="footer">Developed by Team CHIRU</div>', unsafe_allow_html=True)

# Continue with your existing code...
catcol, numcol = [], []

def outli(se_co):
    va = df[se_co].values
    l = []
    m = df[se_co].median()
    q1 = np.quantile(df[se_co], q=0.25)
    q3 = np.quantile(df[se_co], q=0.75)
    iqr = q3 - q1
    lb = q1 - (1.5 * iqr)
    ub = q3 + (1.5 * iqr)
    for j in va:
        if j < lb or j > ub:
            l.append(m)
        else:
            l.append(j)
    return l

def chart(pl, se_co):
    if pl == 'bar':
        v = df[se_co].value_counts()
        if len(v) <= 12:
            sns.countplot(data=df, x=se_co, palette='Set2')
            plt.title(f'BAR GRAPH of {se_co}')
            st.pyplot(plt)
            plt.clf()
    elif pl == 'pie':
        data = df[se_co].value_counts()
        if len(data) <= 12:
            ke = data.keys()
            va = data.values
            plt.pie(va, labels=ke, autopct='%0.2f%%', radius=1)
            plt.title(f'PIE CHART of {se_co}')
            st.pyplot(plt)
            plt.clf()
    elif pl == 'hist':
        df['bal'] = outli(se_co)
        plt.subplot(1, 2, 1)
        plt.hist(df[se_co])
        plt.title(f'{se_co}_before_outliers')
        plt.subplot(1, 2, 2)
        plt.hist(df['bal'])
        plt.title(f'{se_co}_after_outliers')
        st.pyplot(plt)
        plt.clf()
        df.drop('bal', axis=1, inplace=True)
    elif pl == 'dist':
        df['bal'] = outli(se_co)
        plt.subplot(1, 2, 1)
        sns.distplot(df[se_co], kde=True, hist=True)
        plt.title(f'{se_co}_before_outliers')
        plt.subplot(1, 2, 2)
        sns.distplot(df['bal'], kde=True, hist=True)
        plt.title(f'{se_co}_after_outliers')
        st.pyplot(plt)
        plt.clf()
        df.drop('bal', axis=1, inplace=True)
    elif pl == 'boxplot':
        df['bal'] = outli(se_co)
        plt.subplot(1, 2, 1)
        sns.boxplot(df[se_co])
        plt.title(f'{se_co}_before_outliers')
        plt.subplot(1, 2, 2)
        sns.boxplot(df['bal'])
        plt.title(f'{se_co}_after_outliers')
        st.pyplot(plt)
        plt.clf()

def heat():
    cor = df.corr(numeric_only=True)
    sns.heatmap(cor, annot=True, cmap='magma', linewidths=1, linecolor='white')
    plt.title('HEATMAP')
    st.pyplot(plt)
    plt.clf()

def cro(se_col1, se_col2):
    df1 = pd.crosstab(df[se_col1], df[se_col2])
    df1.plot(kind='bar')
    plt.title('CROSSTAB GRAPH')
    st.pyplot(plt)
    plt.clf()

if file is not None:
    file_extension = os.path.splitext(file.name)[-1].lower()
    try:
        if file_extension == '.csv':
            sep = st.text_input('Enter the separator for the CSV file', ',')
            df = pd.read_csv(file, sep=sep)
            cols = df.columns
        elif file_extension == '.xlsx':
            df = pd.read_excel(file)
            cols = df.columns
        else:
            st.error('Unsupported file type. Please upload a .csv or .xlsx')
        st.write(df.head())
        catcol = df.select_dtypes(include='object').columns
        valcol = df.select_dtypes(exclude='object').columns
    except Exception as e:
        st.error(f'Error reading the file: {str(e)}')

se_op = st.sidebar.selectbox('select plot', ['bar', 'pie', 'hist', 'dist', 'boxplot', 'heatmap', 'crosstab'])

if se_op in ['bar', 'pie']:
    se_co = st.sidebar.selectbox('select catcolumn :', catcol)
elif se_op in ['hist', 'dist', 'boxplot']:
    se_co = st.sidebar.selectbox('Select num column', valcol)
elif se_op in ['crosstab']:
    se_col1 = st.sidebar.selectbox('select column 1:', cols)
    se_col2 = st.sidebar.selectbox('select column 2:', cols)

submit = st.sidebar.button('submit')

if submit and file is not None:
    if se_op in ['pie', 'bar', 'hist', 'dist', 'boxplot']:
        chart(se_op, se_co)
    elif se_op in ['heatmap']:
        heat()
    elif se_op in ['crosstab']:
        cro(se_col1, se_col2)
elif submit and file is None:
    st.write('PLEASE UPLOAD THE FILE AND CHECK IT AGAIN')
