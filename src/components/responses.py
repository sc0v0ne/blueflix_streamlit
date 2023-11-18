import pandas as pd
import streamlit as st


def response_recommends(results: pd.DataFrame)-> st.dataframe:    
    st.dataframe(
        results,
        use_container_width=False,        
        )

def response_markdown(text: str) -> st.markdown:
    st.markdown(text)