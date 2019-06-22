''' Image processing functions using opencv'''
import cv2 as cv

def get_image_thresholds(image):
    ''' Get original image with different type of thresholds applied'''
    _, thresh1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
    _, thresh2 = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
    _, thresh3 = cv.threshold(image, 127, 255, cv.THRESH_TRUNC)
    _, thresh4 = cv.threshold(image, 127, 255, cv.THRESH_TOZERO)
    return [thresh1, thresh2, thresh3, thresh4]

def enlarge_image(image):
    ''' Enlarge image size without losing quality'''
    return cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

def reduce_image(image):
    ''' Reduce image size without losing quality'''
    return cv.resize(image, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
