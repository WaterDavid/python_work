import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd

if __name__ == '__main__':
    reviews = pd.read_csv('fandango_scores.csv')
    cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
    norm_reviews = reviews[cols]
    print(norm_reviews[:1])

    num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

    bar_heights = norm_reviews.loc[0, num_cols].values
    # print bar_heights
    bar_positions = arange(5) + 0.75
    # print bar_positions
    fig, ax = plt.subplots()
    ax.bar(bar_positions, bar_heights, 0.5)
    plt.show()

    fig, ax = plt.subplots()
    ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
    ax.set_xlabel('Fandango')
    ax.set_ylabel('Rotten Tomatoes')
    plt.show()

    reviews = pd.read_csv('fandango_scores.csv')
    cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
    norm_reviews = reviews[cols]
    print(norm_reviews[:5])
    fandango_distribution = norm_reviews['Fandango_Ratingvalue'].value_counts()
    fandango_distribution = fandango_distribution.sort_index()

    imdb_distribution = norm_reviews['IMDB_norm'].value_counts()
    imdb_distribution = imdb_distribution.sort_index()

    print(fandango_distribution)
    print(imdb_distribution)

    fig, ax = plt.subplots()
    ax.hist(norm_reviews['Fandango_Ratingvalue'])
    # ax.hist(norm_reviews['Fandango_Ratingvalue'],bins=20)
    # ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(4, 5),bins=20)
    plt.show()

    fig, ax = plt.subplots()
    ax.boxplot(norm_reviews['RT_user_norm'])
    ax.set_xticklabels(['Rotten Tomatoes'])
    ax.set_ylim(0, 5)
    plt.show()

    num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
    fig, ax = plt.subplots()
    ax.boxplot(norm_reviews[num_cols].values)
    ax.set_xticklabels(num_cols, rotation=90)
    ax.set_ylim(0, 5)
    plt.show()
