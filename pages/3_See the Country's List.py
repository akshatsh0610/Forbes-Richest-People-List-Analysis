import pandas as pd
import numpy as np
import streamlit as st

from pathlib import Path
data=Path(__file__).parents[1] / 'pages/forbes_richman.csv'

df=pd.read_csv(data,encoding='latin-1')

import sys
class Foobar:
    pass
def str_to_class(str):
    return getattr(sys.modules[__name__], str)

st.markdown("# Enter the name of country")
title = st.text_input('Please enter country', 'Country')
s=str_to_class(title)
if s=='Country' or s=="":
    st.write('')
else:
    if s in df['Country']:
        df1=df[df['Country']==s]
        st.table(df1)