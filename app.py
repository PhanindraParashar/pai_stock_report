import streamlit as st
from utils import *



with open('Data.json','r') as f:
    data = json.load(f)

with open('map_files.json','r') as f:
    map_files = json.load(f)


def load_page(company_name):
    file = map_files[company_name]
    j = data[company_name]
    
    st.markdown(f'# {j["company_name"]}')
    for val in j['analysis_json'].keys():
        # write markdown 
        st.markdown(f'## {title_map[val]}')
        st.markdown(j['analysis_json'][val])



companies_list = list(map_files.keys())
# select 1 company from the list dropdown
company_name = st.selectbox('Select Company', companies_list)

load_page(company_name)
    