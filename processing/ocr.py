''' OCR functions using tesseract '''
import cv2 as cv
import pytesseract as tesseract
import processing.optimizer as optimizer
import processing.parser as parser
from utils.const import ResizeTypes
tesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def get_image_text(filename):
    ''' Get text from image using tesseract '''
    img = cv.imread(filename, 0)
    return parser.clean_text(tesseract.image_to_string(img))

def get_threshold_image_text(filename, resize_type):
    ''' Get text from image using different types of threshold '''
    img = cv.imread(filename, 0)
    if resize_type == ResizeTypes.ENLARGE:
        img = optimizer.enlarge_image(img)
    elif resize_type == ResizeTypes.REDUCE:
        img = optimizer.reduce_image(img)
    images = optimizer.get_image_thresholds(img)
    return [parser.clean_text(tesseract.image_to_string(img)) for img in images]

def get_enlarged_image_text(filename):
    ''' Get text from image with double size '''
    img = cv.imread(filename, 0)
    img_large = optimizer.enlarge_image(img)
    return parser.clean_text(tesseract.image_to_string(img_large))

def get_reduced_image_text(filename):
    ''' Get text from image with half size '''
    img = cv.imread(filename, 0)
    img_small = optimizer.enlarge_image(img)
    return parser.clean_text(tesseract.image_to_string(img_small))

def get_resized_image_text(filename):
    ''' Get text from image using different sizes '''
    img = cv.imread(filename, 0)
    img_large = optimizer.enlarge_image(img)
    img_small = optimizer.reduce_image(img)
    return [parser.clean_text(tesseract.image_to_string(img)) for img in [img_large, img_small]]

def save_images(images, filename):
    ''' Auxiliar function - Save list of images as files'''
    name = filename.split('.')[0]
    extension = filename.split('.')[1]
    index = 0
    for img in images:
        cv.imwrite(f'{name}-{str(index)}.{extension}', img)
        index += 1
