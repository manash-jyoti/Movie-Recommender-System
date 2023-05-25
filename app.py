# importing all the necessary modules
import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np
from PIL import Image

# setting the page configuration
st.set_page_config(layout="wide")
my_api = 'a411ad96b2c8f1ba4aa8f0c83d780482'

# function to fetch poster and relevant information
def fetch_details(movie_id):
    user_agents_list = [
        'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36']

    headers = {'User-Agent': np.random.choice(user_agents_list)}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={my_api}'
    response = requests.get(url, headers=headers)
    data = response.json()
    poster_path = data['poster_path']
    imdb_id = data['imdb_id']
    overview = data['overview']
    release = data['release_date']
    runtime = str(data['runtime'])+" min"
    vote_avg = round(data['vote_average'],2)

    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path, imdb_id, overview, release, runtime, vote_avg

# recommender function
def recommender(movie):
    movie_index = movies[movies["Title"] == movie].index[0]  # to extract movie information

    how_similar = similiarity[movie_index]  # access the list element with index = movie_index
    index_dist_pair = sorted(list(enumerate(how_similar)), key=lambda x: x[1], reverse=True)[
                      1:6]  # extract the top 5 recommended movies

    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_IMDb = []
    recommended_movies_story = []
    recommended_movies_release = []
    recommended_movies_runtime = []
    recommended_movies_avg_vote = []

    for i in index_dist_pair:
        recommended_movies.append(movies.iloc[i[0]].Title)
        movie_id = movies.iloc[i[0]].Movie_id
        Poster, IMDb_id, Overview, Release_date, Runtime, Vote_average = fetch_details(movie_id)
        recommended_movies_poster.append(Poster)
        recommended_movies_IMDb.append(IMDb_id)
        recommended_movies_story.append(Overview)
        recommended_movies_release.append(Release_date)
        recommended_movies_runtime.append(Runtime)
        recommended_movies_avg_vote.append(Vote_average)

    return recommended_movies, recommended_movies_poster, recommended_movies_IMDb, recommended_movies_story,recommended_movies_release, recommended_movies_runtime, recommended_movies_avg_vote

img = Image.open('logo.png')
img = img.resize((200, 200), )
st.image(img, use_column_width=False)
st.title("Movie Recommender System")

# loading files from the directory
movie_data = pickle.load(open('movies.pkl',"rb"))
similiarity = pickle.load(open('similarity.pkl',"rb"))

movies = pd.DataFrame(movie_data)
option = st.selectbox(
    'Select the movie of your choice:',
    movies["Title"].values)

if st.button('Recommend'):
    movie_names, movie_posters, imdbID, story, releaseDate, runTime, avgVote =recommender(option)

    num_columns = 5
    columns = st.columns(num_columns)

    for i in range(num_columns):
        with columns[i]:
            st.subheader(movie_names[i])
            st.image(movie_posters[i])
            st.markdown(f"**:green[IMDb ID:]** {imdbID[i]}")
            st.markdown(f"**:green[Story:]** {story[i]}")
            st.markdown(f"**:green[Release Date:]** {releaseDate[i]}")
            st.markdown(f"**:green[Runtime:]** {runTime[i]}")
            st.markdown(f"**:green[Average Vote:]** ⭐{avgVote[i]}")