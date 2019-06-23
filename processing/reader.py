''' Dataset manipulation functions with pandas '''
import pandas as pd
from utils.const import DATASET_ROUTE, DATASET_GENRES_COLUMNS, DATASET_VOTES_COLUMNS

def get_dataset_votes():
    '''
    Get dataset from CSV file as Pandas DataFrame
    -> Filter useful columns (title, vote average, genres)
    -> Filter useful examples (with vote average > 0)
    '''
    dataset = pd.read_csv(DATASET_ROUTE)
    dataset = dataset[DATASET_VOTES_COLUMNS]
    dataset = dataset[dataset.vote_average > 0]

    return dataset.values

def get_dataset_genres(genres_set):
    '''
    Get dataset from CSV file as Pandas DataFrame
    -> Filter useful columns (Title, genres)
    -> Filter useful examples (with genres not empty)
    -> Parse genres by id
    '''
    dataset = pd.read_csv(DATASET_ROUTE)
    dataset = dataset[DATASET_GENRES_COLUMNS]
    dataset = dataset[(dataset.genres != '') & (dataset.genres != '[]')]

    genres = dataset.loc[:, 'genres']
    genres = genres.apply(lambda row: parse_genre(row, genres_set))

    dataset = dataset.drop(columns=['genres'])
    dataset['genres'] = genres

    return dataset.values

def get_genres():
    ''' Get list of distinct genre objects '''
    dataset = pd.read_csv(DATASET_ROUTE)
    dataset = dataset[['genres']]
    genres = []
    for _, item in dataset['genres'].iteritems():
        genre_list = eval(item)
        for genre in genre_list:
            if genre not in genres:
                genres.append(genre)
    index = 0
    for genre in genres:
        genre['internal_id'] = index
        index += 1
    return genres

def parse_genre(genre, genres_set):
    ''' Auxiliar function to get id from genre object string '''
    genre_list = eval(genre)
    genre_id = genre_list[0]['id']
    genre_internal_id = [g['internal_id'] for g in genres_set if g['id'] == genre_id][0]
    return genre_internal_id
