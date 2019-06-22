''' Image managing functions'''
from os import listdir
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError
from utils.const import IMAGE_FOLDER, ResizeTypes, ThresholdTypes
import processing.ocr as ocr

def get_images():
    '''Get list of image names'''
    return listdir(IMAGE_FOLDER)

def post_image(image_name, image_url, resize_type, threshold_type):
    '''Get image from url and save it locally'''
    try:
        urlretrieve(image_url, IMAGE_FOLDER + image_name)
    except (URLError, HTTPError):
        return {'error': 'Could not retrieve image from URL'}
    return get_image_by_name(image_name.split('.')[0], resize_type, threshold_type)

def get_image_by_name(name, resize_type, threshold_type):
    '''Get image data searching by name'''
    images = [p for p in listdir(IMAGE_FOLDER) if p.split('.')[0] == name]
    if not images:
        return {}

    image_text = ocr.get_image_text(IMAGE_FOLDER + images[0])
    result = {
        'name': images[0],
        'text': image_text,
    }

    if resize_type == ResizeTypes.ENLARGE:
        resized_image_text = ocr.get_enlarged_image_text(IMAGE_FOLDER + images[0])
        result['resized'] = {
            'enlarged': resized_image_text
        }
    elif resize_type == ResizeTypes.REDUCE:
        resized_image_text = ocr.get_reduced_image_text(IMAGE_FOLDER + images[0])
        result['text_resized'] = {
            'reduced': resized_image_text
        }
    elif resize_type == ResizeTypes.BOTH:
        resized_image_text = ocr.get_resized_image_text(IMAGE_FOLDER + images[0])
        result['text_resized'] = {
            'enlarged': resized_image_text[0],
            'reduced': resized_image_text[1],
        }

    if threshold_type == ThresholdTypes.ALL:
        threshold_image_text = ocr.get_threshold_image_text(IMAGE_FOLDER + images[0], resize_type)
        result['text_thresholded'] = {
            'binary': threshold_image_text[0],
            'binary_inv': threshold_image_text[1],
            'trunc': threshold_image_text[2],
            'to_zero': threshold_image_text[3],
        }

    return result
