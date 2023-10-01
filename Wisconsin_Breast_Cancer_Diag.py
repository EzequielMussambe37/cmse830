# pylint: disable=no-member
import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
import altair as alt

layout = "centered" #centered
page_title = "Wisconsin Breast Cancer Diagnostic"
plots = ["", "pairplot","hist",]
hue = None
#page_icon = ":money_with_wings:"

st.set_page_config(page_title,layout)
st.title(page_title)

"---"
df = pd.read_csv("data.csv")
fig = plt.figure(figsize=(9,7))

#Expand the table;;;;
with st.expander("Show Data Table"):
    df


"---"
st.header("Data visualization")
df_2 = df[["diagnosis", "concave points_mean","perimeter_mean","radius_mean"]]

columns =  df.columns.values.tolist()
columns[0] = None
print(columns)
col1, col2 ,col3= st.columns(3)

plot_type = col1.selectbox("Select Plot Type:", plots)
hue = col2.selectbox("Select Hue:", columns)
if plot_type == "pairplot" and hue != "":

    sns.pairplot(df_2,hue=hue)
    plt.title("Perimeter Mean")
    st.pyplot(plt.gcf()) # get current figure

if plot_type == "hist" :
    feature = col3.selectbox("Select Feature:", columns)
    if feature != "":
        sns.histplot(
            data=df,
            x=feature,
            hue=hue,
            multiple="stack"
        )

        plt.title("Perimeter Mean")
        st.pyplot(plt.gcf()) # get current figure