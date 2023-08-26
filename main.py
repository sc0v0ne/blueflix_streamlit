import pandas as pd
import streamlit as st
from src.components import query


def load_data():
    df = pd.read_csv('src/data/final/dataset_titles_final.csv', sep=',')
    return df
DF = load_data()

st.set_page_config(page_title="Blueflix",
                   page_icon="🍿",
                   layout="centered",
                   initial_sidebar_state="collapsed",
                   menu_items={
                       'Get Help':
                       'https://www.extremelycoolapp.com/help',
                       'Report a bug':
                       "https://www.extremelycoolapp.com/bug",
                       'About':
                       "# This is a header. This is an *extremely* cool app!"
                   })

st.title(' 📽️🍿 Blueflix')

st.markdown("😀 Hey!!!,  how are you ?")

st.markdown("This project I developed to apply skills that I am learning.")

st.markdown("I was happy to look for recommendations.")

st.markdown(
    "If you can help by giving my project a star, I really appreciate it.")

title = st.text_input('Enter the title you are looking for', 'Monster Maker')
top = st.text_input('Enter number of recommendations', 10)

if st.button('Recommendations'):
    df_query = query.query_name_title(DF, title, top)
    
    st.dataframe(df_query, use_container_width=True)
