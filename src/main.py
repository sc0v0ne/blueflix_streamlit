import pandas as pd
import streamlit as st
from components.query import recommends


def load_data():
    df = pd.read_csv('./src/data/final/dataset_titles_final.csv', sep=',')
    return df
DF = load_data()

st.set_page_config(page_title="Blueflix",
                   page_icon="🍿",
                   layout="wide",
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

st.markdown("Extra Columns:")

duration_seconds = st.checkbox('Duration Seconds')
director = st.checkbox('Director')
country = st.checkbox('Country')
channel_streaming = st.checkbox('Channel Streaming')

extra_cols = {
    'duration_seconds': duration_seconds,
    'director': director,
    'country': country,
    'channel_streaming': channel_streaming,

}

if st.button('Recommendations'):

    recommends(DF, title, top, extra_cols)

