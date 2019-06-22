''' Parser file for different constants '''
from utils.const import ResizeTypes, ThresholdTypes

def get_resize_type(resize_type):
    ''' Parse number to resize type constant '''
    if resize_type == '1':
        return ResizeTypes.ENLARGE
    if resize_type == '2':
        return ResizeTypes.REDUCE
    if resize_type == '3':
        return ResizeTypes.BOTH
    return ResizeTypes.NONE

def get_threshold_type(threshold_type):
    ''' Parse number to threshold type constant '''
    if threshold_type == '1':
        return ThresholdTypes.ALL
    return ThresholdTypes.NONE
