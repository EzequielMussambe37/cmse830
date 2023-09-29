# pylint: disable=no-member
import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_wine
import altair as alt
#wine_data = load_wine()
iris_dataset = sns.load_dataset("iris")
#print(wine_data)

#labels = wine_data.feature_names
#argets = wine_data.target
#print(labels)
df_form = iris_dataset
#df_form['targets'] = targets
st.write("""
# IRIS Dataset
How are petal_with and petal_length correlated?
""")
alt_handle = alt.Chart(df_form).mark_circle(size=60).encode(x='petal_width', y='petal_length',
    color='species', tooltip=['sepal_length', 'sepal_width']).interactive()
st.altair_chart(alt_handle)