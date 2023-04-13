import pandas as pd
import numpy as np
import streamlit as st

from pathlib import Path
data=Path(__file__).parents[1] / 'pages/forbes_richman.csv'

df=pd.read_csv(data,encoding='latin-1')



st.markdown("# Enter the name of person")
s = st.text_input('Name', 'Name')
if s=='Name' or s=="":
    st.write('')
else:
    if s in df['Name'].values:
        # st.markdown(type(s))
        df1=df[df['Name']==s]
        st.table(df1)
    else:
        st.markdown("# No data present")