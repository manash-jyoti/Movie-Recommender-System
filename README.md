# Movie Recommendation System

This is a movie recommendation system developed using Python, utilizing a dataset sourced from Kaggle. The dataset contains information on 10,000 movies, including attributes such as genres, keywords, cast, crew, and overviews. A combined column named "tags" was created, aggregating the relevant attributes to form a basis for movie recommendations.

The recommendation system employs a content-based filtering approach using Cosine Similarity. The textual information in the "tags" column is transformed using CountVectorizer, enabling the calculation of similarity scores between movies.


## Features

- Allows users to select a movie of their choice
- Generates a list of the top five recommended movies along with their informations based on similarity


## Dataset

The datasets used in this project are obtained from Kaggle and contain 10,000 movies and credits with various attributes. You can find the datasets [here](https://www.kaggle.com/datasets/gazu468/tmdb-10000-movies-dataset).
## Setup

To run the movie recommendation system locally, follow these steps:

1. Clone the repository:

git clone https://github.com/your_username/repo_name.git

2. Install the required dependencies:

!pip install -r requirements.txt

3. Run the Streamlit web app:

streamlit run app.py
## Usage/Examples

1. Open the web app in your browser.
2. Select a movie from the provided options or use the search functionality to find a specific movie.
3. The system will generate a list of the top five recommended movies based on similarity to the selected movie.


## Technologies used

Python
Pandas
Scikit-learn
Natural language toolkit
Streamlit


## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.


## License

License
This project is licensed under the MIT License [MIT](https://choosealicense.com/licenses/mit/)


## Demo

Movie recommender system demo [33ff9e3a-a02a-47af-be90-fe03775c161e.webm](https://github.com/manash-jyoti/Netflix-dashboard/assets/90838725/33d9c65d-c32a-4c68-ae97-0199aef3da1b)

