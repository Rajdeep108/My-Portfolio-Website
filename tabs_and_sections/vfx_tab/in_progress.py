# importing dependencies
import streamlit as st
from functions import *

def work_in_progress_section():
        custom_anchor("to be continued")
        st.header(''':red[OOPS  :(]''')
        vertical_space(2)
        st.markdown('''
                :orange[This page is under construction.]
                \n
                :green[Stay tuned for updates. More amazing content is coming soon! ]
                ''')
        vertical_space(2)
        st.status("This section is going to be UPDATED SOON !!",state="error")
