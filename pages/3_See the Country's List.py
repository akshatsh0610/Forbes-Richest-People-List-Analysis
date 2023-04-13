import pandas as pd
import numpy as np
import streamlit as st

from pathlib import Path
data=Path(__file__).parents[1] / 'pages/forbes_richman.csv'

df=pd.read_csv(data,encoding='latin-1')



st.markdown("# Enter the name of country")
s = st.text_input('Please enter country', 'Country')
if s=='Country' or s=="":
    st.write('')
else:
    if s in df['Country'].values:
        # st.markdown(type(s))
        df1=df[df['Country']==s]
        st.table(df1)
    else:
        st.markdown("# No data present")