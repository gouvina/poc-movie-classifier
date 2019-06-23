''' Constants file'''
from enum import Enum

# File system routes
IMAGES_ROUTE = 'data/pictures/'
MODELS_ROUTE = 'data/models/'
DATASET_ROUTE = 'data/movies_metadata_big.csv'
MODEL_VOTES_ROUTE = 'data/models/model_votes.h5'

# Dataset constants
DATASET_GENRES_COLUMNS = ['title', 'genres']
DATASET_VOTES_COLUMNS = ['title', 'vote_average']

# Parameter types
class ResizeTypes(Enum):
    ''' 4 types of operation related to image size '''
    NONE = 0
    ENLARGE = 1
    REDUCE = 2
    BOTH = 3

class ThresholdTypes(Enum):
    ''' 2 types of operation related to image threshold '''
    NONE = 0
    ALL = 1
