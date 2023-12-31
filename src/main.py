import os
import pandas as pd
import streamlit as st
from components.query import recommends, recommender_by_gender

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

def load_data(
            dir_data: str,
            name_dataset: str
            ) -> pd.DataFrame:
    path_data = os.path.join('./src/data', dir_data, name_dataset)
    df = pd.read_csv(f'{path_data}.csv', sep=',')
    return df

DF = load_data('final', 'dataset_titles_final')
DF_GENDER = load_data('processed', 'train_gender')
COLS = DF_GENDER.columns


st.title(' 📽️🍿 Blueflix')

st.markdown("😀 Hey!!!,  how are you ?")

st.markdown("This project I developed to apply skills that I am learning.")

st.markdown("I was happy to look for recommendations.")

st.markdown("If you can help by giving my project a star, I really appreciate it.")

col1, col2 = st.columns(2)

with col1:
    st.header("Recommends")
    title = st.text_input('Enter the title you are looking for', 'Monster Maker')
    top = st.text_input('Enter number of recommendations', 10)

with col2:
    st.header("Extra Columns")

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

st.markdown('------------------------')

st.title(' Select by Genre 📽️🍿 ')

options = st.multiselect(
    'In the menu select up to 3 types of movie or TV show genres:',
    COLS,
    max_selections=3,
    )

if st.button('Search'):

    recommender_by_gender(DF, options, COLS)
