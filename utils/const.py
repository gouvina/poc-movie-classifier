''' Constants file'''
from enum import Enum

# File system routes
IMAGE_FOLDER = 'data/pictures/'

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
