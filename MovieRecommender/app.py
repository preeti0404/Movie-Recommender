import streamlit as st
import pickle
import pandas as pd 
import requests
import os
path = os.path.dirname(__file__)
# my_file = path+'/photo.png'
moviesDict = pickle.load(open(path + '/movies_dict.pkl','rb'))
movies = pd.DataFrame(moviesDict)
similarity = pickle.load(open(path + '/similarity.pkl','rb'))

def fetchPoster(movieId):
    res = requests.get(f"https://api.themoviedb.org/3/movie/{movieId}?api_key=5af00bcf1269c9513cf7a73ee264e94f&language=en-US")
    data = res.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movieIndex = movies[movies['title'] == movie].index[0]
    distances = similarity[movieIndex]
    moviesList = sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:6]
    
    recommendedMovies = []
    recommendedMoviesPosters = []
    
    for item in moviesList:
        movieId = movies.iloc[item[0]].movie_id
        recommendedMovies.append(movies.iloc[item[0]].title)
        recommendedMoviesPosters.append(fetchPoster(movieId))
        
    return recommendedMovies,recommendedMoviesPosters
    

st.title("Movie Recommender System")

selectedMovieName = st.selectbox(
     'How would you like to be contacted?',
     movies['title'].values)

if st.button('Recommend'):
    recommendations,posters = recommend(selectedMovieName)
    # for movie in recommendations:
    #     st.write(movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])
