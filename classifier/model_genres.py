''' A '''
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, utils
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import processing.reader as reader

class TrainCallback(Callback):
    ''' A '''
    def on_epoch_end(self, epoch, logs):
        ''' A '''
        if epoch % 100 == 0:
            print(f'Iteration n°{epoch} reached')

class ModelGenres():
    ''' A '''
    def __init__(self):

        self.all_genres = reader.get_genres()
        self.dataset = reader.get_dataset_genres(self.all_genres)

        self.titles = self.dataset[:, 0]
        self.train_titles = None
        self.test_titles = None

        self.genres = self.dataset[:, 1]
        self.train_genres = None
        self.test_genres = None

        self.model = None
        self.history = None

        self.vectorizer = None
        self.epochs = 1000

        self.vectorize_dataset()
        self.split_dataset()

    # GETTERS & SETTERS

    def get_dataset(self):
        ''' A '''
        return self.dataset

    def get_test_dataset(self):
        ''' A '''
        return self.test_titles

    def get_test_labels(self):
        ''' A '''
        return self.test_votes

    # MAIN FUNCTIONS

    def train(self):
        ''' A '''

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
                                      self.genres,
                                      epochs=self.epochs,
                                      validation_split=0.2,
                                      verbose=0,
                                      callbacks=[TrainCallback()])

        #print(self.model.summary())

    def classify(self, examples):
        ''' A '''
        return self.model.predict(examples)

    # DATA MANIPULATION FUNCTIONS

    def vectorize_dataset(self):
        ''' A '''
        self.vectorizer = CountVectorizer(stop_words='english')
        self.titles = self.vectorizer.fit_transform(self.titles).toarray()

    def split_dataset(self):
        ''' A '''
        train_ds, test_ds, train_lbls, test_lbls = train_test_split(
            self.titles, self.genres, test_size=0.2)

        self.train_titles = train_ds
        self.test_titles = test_ds

        self.train_genres = train_lbls
        self.test_genres = test_lbls

    # FILE MANIPULATION FUNCTIONS

    def save_model(self, filename):
        ''' A '''
        self.model.save(filename)

    def load_model(self, filename):
        ''' A '''
        self.model = keras.models.load_model(filename)
