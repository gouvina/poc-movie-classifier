''' Model managing functions'''
from classifier.model_votes import ModelVotes
from utils.const import MODEL_VOTES_ROUTE

def create_models():
    ''' Generate and train both models '''
    model_votes = ModelVotes()
    model_votes.train()

    save_models(model_votes)

    return model_votes

def load_models():
    ''' Load both pre-trained models '''
    model_votes = ModelVotes()
    model_votes.load_model(MODEL_VOTES_ROUTE)

    return model_votes

def save_models(model):
    ''' Save trained models to file '''
    model.save_model(MODEL_VOTES_ROUTE)
