''' Regression model representation '''
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, utils
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.feature_extraction.text import CountVectorizer
import processing.reader as reader

class TrainCallback(Callback):
    ''' Callback class for showing train progress '''
    def on_epoch_end(self, epoch, _):
        ''' Print info after iteration '''
        if epoch % 10 == 0:
            print(f'Iteration n° {epoch} reached')

class ModelVotes():
    '''
    Representation for rating model
    -> Neural network with functions for training and predicting
    -> Vectorizer for text interpretation
    -> File manipulation for saving/loading models
    '''
    def __init__(self):

        self.dataset = reader.get_dataset_votes()

        self.titles = self.dataset[:, 0]
        self.votes = self.dataset[:, 1]

        self.model = None
        self.history = None

        self.vectorizer = None
        self.epochs = 100

        self.vectorize_dataset()

    # GETTERS & SETTERS

    def get_dataset(self):
        ''' Getter for pure dataset '''
        return self.dataset

    def get_titles(self):
        ''' Getter for dataset rows '''
        return self.titles

    def get_votes(self):
        ''' Getter for dataset labels '''
        return self.votes

    # MAIN FUNCTIONS

    def train(self):
        ''' Generate and train neural network '''

        self.model = keras.Sequential([
            layers.Dense(100,
                         activation=tf.nn.relu,
                         input_shape=[len(self.vectorizer.get_feature_names())]),
            layers.Dense(100, activation=tf.nn.relu),
            layers.Dense(1)
        ])

        self.model.compile(loss='mse',
                           optimizer='rmsprop',
                           metrics=['mse', 'mae'])

        self.history = self.model.fit(self.titles,
                                      self.votes,
                                      epochs=self.epochs,
                                      validation_split=0.2,
                                      verbose=0,
                                      callbacks=[TrainCallback()])

        #print(self.model.summary())

    def predict(self, examples):
        ''' Predict a set of examples with trained model '''
        prediction = self.model.predict(examples)
        result = np.zeros(prediction.size)
        for i in range(0, prediction.size):
            result[i] = int(round(prediction[i][0]))
        return result

    # DATA MANIPULATION FUNCTIONS

    def vectorize_dataset(self):
        ''' Generate sparse matrix from vectorized titles '''
        self.vectorizer = CountVectorizer(stop_words='english')
        self.titles = self.vectorizer.fit_transform(self.titles).toarray()

    def vectorize_examples(self, examples):
        ''' Generate sparse matrix from vectorized examples '''
        return self.vectorizer.transform(examples).toarray()

    # FILE MANIPULATION FUNCTIONS

    def save_model(self, filename):
        ''' Save model into file with filename '''
        self.model.save(filename)

    def load_model(self, filename):
        ''' Load model from file with filename '''
        self.model = keras.models.load_model(filename)
