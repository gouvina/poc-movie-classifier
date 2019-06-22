''' API main and routes'''
from flask import Flask, jsonify, request
import controllers.image_controller as image_controller
import utils.params as params

APP = Flask(__name__)

@APP.route('/images', methods=['GET'], endpoint='get_images')
def get_images():
    ''' GET list of saved image names '''
    images = image_controller.get_images()
    return jsonify(images)

@APP.route('/images/<image_name>', methods=['GET'], endpoint='get_image_by_name')
def get_image_by_name(image_name):
    ''' GET object with image data '''
    resize = params.get_resize_type(request.args.get('resize'))
    threshold = params.get_threshold_type(request.args.get('threshold'))
    image = image_controller.get_image_by_name(image_name, resize, threshold)
    return jsonify(image)

@APP.route('/images', methods=['POST'], endpoint='post_image')
def post_image():
    ''' POST object with image data '''
    image_name = request.values['name']
    image_url = request.values['url']
    resize = params.get_resize_type(request.values.get('resize'))
    threshold = params.get_threshold_type(request.values.get('threshold'))
    result = image_controller.post_image(image_name, image_url, resize, threshold)
    return jsonify(result)

APP.run()
