import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st

from pathlib import Path
data=Path(__file__).parents[1] / 'pages/forbes_richman.csv'

plt.rcParams.update({'font.size': 22})

st.title('Forbes Complete List Analysis')
df=pd.read_csv(data,encoding='Latin-1')
df=df.drop_duplicates()
df=df.iloc[0:2509,:]

st.markdown("# Data")
st.dataframe(df)

st.markdown("# Industry Data for every Country")
df1=df.groupby(['Country','Industry'])['Name'].count()
df1.to_csv('industry.csv')
df1=pd.read_csv('industry.csv')
df1=pd.pivot_table(df1,values=None,index=['Country'],columns=['Industry'],fill_value=0,aggfunc=np.sum)
st.checkbox("Use container width", value=False, key="use_container_width")
st.dataframe(df1, use_container_width=st.session_state.use_container_width)

st.markdown("# Country wise analysis")
fig1=plt.figure(figsize = (50,26))
ax = sns.countplot(x=df['Country'],order = df['Country'].value_counts().index)
plt.xticks(rotation=90)
st.pyplot(fig1)

st.markdown("# Industry wise analysis")
fig2=plt.figure(figsize = (16,10))
ax = sns.countplot(x=df['Industry'],order = df['Industry'].value_counts().index)
plt.xticks(rotation=90)
st.pyplot(fig2)

st.markdown("# Age wise analysis")
fig3=plt.figure(figsize = (30,10))
ax = sns.countplot(x=df['Age'],order = df['Age'].value_counts().index)
plt.xticks(rotation=90)
st.pyplot(fig3)