import pandas as pd
import streamlit as st


def response_recommends(
                    results: pd.DataFrame
                    )-> st.dataframe:
    """Show component st.dataframe, adapted to dataframe

    Args:
        results (pd.DataFrame): Dataset

    Returns:
        st.dataframe: Show component st.dataframe adapted
    """
    try:
        results = results.reset_index(drop=True)
        results['title'] = results['title'].apply(lambda x: x.title())
        results['director'] = results['director'].apply(lambda x: x.capitalize())
    except Exception:
        pass


    st.dataframe(
        results,
        use_container_width=True,
        hide_index=True,
        column_config={
            "title": "Title",
            "duration_seconds": "Title",
            "director": "Director",
            "country": "Country",
            "channel_streaming": "Channel Streaming",
            "gender_type": "Genres",

        },
        )

def response_markdown(text: str) -> st.markdown:
    """Show text in text markdwon

    Args:
        text (str): text input

    Returns:
        st.markdown: Show component markdown
    """
    st.markdown(text)