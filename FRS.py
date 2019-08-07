__author__ = "T Murder"
__copyright__ = "Nope!"
__credits__ = "T Murder"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "tylrrc@gmail.com"
__status__ = "Under construction"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

sns.set_style('dark')
warnings.filterwarnings('ignore')

movies = pd.read_csv("filmData/ml-latest-small/movies.csv")

ratings = pd.read_csv("filmData/ml-latest-small/ratings.csv")

movie_ratings_combo = pd.merge(movies, ratings, on='movieId')

ratings_mean_count = pd.DataFrame(movie_ratings_combo.groupby('title')['rating'].mean())

ratings_mean_count['rating_counts'] = pd.DataFrame(movie_ratings_combo.groupby('title')['rating'].count())

UMR = movie_ratings_combo.pivot_table(index='userId', columns='title', values='rating')

selection = input("Enter a film on which to base recommendations: ")

selection_row = UMR[selection]

similar = UMR.corrwith(selection_row)

corrFG = pd.DataFrame(similar, columns=['Correlation'])
corrFG.dropna(inplace=True)

corrFG = corrFG.join(ratings_mean_count['rating_counts'])

print(corrFG[corrFG ['rating_counts']>50].sort_values('Correlation', ascending=False).head(25))



