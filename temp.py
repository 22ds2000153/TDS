# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import streamlit as st

st.title('Multiply 2 numbers')


x = st.slider('Select a value')
y = st.slider('Select another value')
st.write(x, 'multiplied by',y,'is', x * y)


