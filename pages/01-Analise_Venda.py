import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import locale

import seaborn as sns


#CONFIGURAÇÃO PAGINA
st.set_page_config(layout='wide', page_title='Analise Vendas',initial_sidebar_state="collapsed")
st.header('Analises De Vendas')

