# TODO: Mechanism to compare genre lists
# TODO: Create empty structure to hold final recommendation scores
import warnings

import pandas as pd

warnings.filterwarnings('ignore')

master = pd.read_csv("dataset/MasterSet.csv")

selection = input("Enter a film on which to base recommendations: ")

temp = master.loc[master['title'] == selection.lower()]

if(temp.empty):
    print("NOT FOUND")
    exit()
else:
    print('Found it!')
    print(temp.to_string())
#print(selection_row.to_string()) #"selection_row"== Left column: Critic ID::::::Right column: Critic score
                                 # If a critic didn't vote on the movie, a value of NaN is seen as opposed to a score.
                                 # If a critic DID vote, then a 0.0-5.0 score is seen.

#print(ratings_mean_count.to_string())

#similar = user_movie_rating.corrwith(selection_row)

#corrFG = pd.DataFrame(similar, columns=['Correlation'])
#corrFG.dropna(inplace=True)

#corrFG = corrFG.join(ratings_mean_count['rating_counts'])

#print(corrFG[corrFG ['rating_counts']>50].sort_values('Correlation', ascending=False).head(25))
exit()


