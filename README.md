# Movie Classifier
Basic REST API for classifying movies based on poster picture

### API Usage
This API allows you to send and image of a movie poster and get its title and possible rating using a neural network.

For mounting the API, run ` python api.py `. It will mount it on port 5000 and make it available to new requests.

It has 2 methods for processing poster images:
- **POST /images**
> Download image from url, extract text with ocr and get its rating with model. <br>
> Request body params: <br>
```json
body: {
    "name": "poster.jpg",
    "url": "<url>",
    "threshold (optional)": 1
}
```
- **GET /images/<image_name>**
> If _<image_name>_ was previously downloaded or included in _data/pictures_, extract text with ocr and get its rating with model. <br>
> Request query params: <br>
> - threshold = 0 (none) 1 (all)
> - resize = 0 (none) 1 (enlarge) 2 (reduce) 3 (both)

**Comments:** If no threshold option is provided, it will predict rating using just one text. Otherwise, it will predict rating for original text and text extracted from each kind of thresholded image.

### Model Usage

For training the model, run ` python train.py `. It will train and save the model in a file (*data/models/model_votes.h5*) that can be loaded afterwards for predicting movie ratings by the API.

**Comments:** Model file is already provided and trained using _data/movies_dataset_big.csv_. Take into account that if _train.py_ is executed and finished, it will overwrite that file.

### Components
* REST API (with *Flask*)
> --> **GET /images** - Retrieves list of saved image's names <br>
> --> **GET /images/<image_name>** - Retrieves saved image's info by name <br>
> --> **POST /images** - Downloads image from url and retrieves its info <br> <br>

* OCR Module (with *Tesseract*, *OpenCV*, *re*)
> --> Process image with *OpenCV* (change size, change threshold) <br>
> --> Extract text from image with *Tesseract* <br>
> --> Delete strange characters and spaces with *re* <br>

* Rating model (with *Tensorflow*, *Keras*, *Sklearn*, *Numpy*, *Pandas*)
> --> Read and process movies dataset with *pandas* <br>
> --> Vectorize movie titles with *CountVectorizer* from *sklearn* <br>
> --> Predict movie rating with *Keras* from *Tensorflow* using a pretrained 2 layered neural network <br>

### Current issues
* REST API methods are insecure, specially **POST /images**, which does not check secure URL before saving its content.
* OCR accuracy is pretty low, some preprocessing has been made with *OpenCV* to help it but it is not enough to get good results.
* Neural network's efficency has not been tested with any metrics yet.
