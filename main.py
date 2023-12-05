# streamlit run main.py
import streamlit as st
import pickle
import pandas as pd
import requests

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movie_df = pd.DataFrame(movie_dict)

cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))

titles = movie_df['title']
tmdbId = movie_df['id']
indices = pd.Series(movie_df.index, index=movie_df['title'])
def content_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return list(tmdbId.iloc[movie_indices].values), list(titles.iloc[movie_indices].values)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e0f4fd52b5503ee92bf73319afeee1ad'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']

st.title('Hybrid movie recommender')

option = st.selectbox(
    'Content based',
    movie_df['title'].values)

if st.button("Recommend", type="primary"):
    tmdbIds, names = content_recommendations(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(fetch_poster(tmdbIds[0]))

    with col2:
        st.text(names[1])
        st.image(fetch_poster(tmdbIds[1]))

    with col3:
        st.text(names[2])
        st.image(fetch_poster(tmdbIds[2]))

    with col4:
        st.text(names[3])
        st.image(fetch_poster(tmdbIds[3]))

    with col5:
        st.text(names[4])
        st.image(fetch_poster(tmdbIds[4]))



