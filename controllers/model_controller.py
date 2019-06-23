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

def predict_examples(examples):
    ''' Load models, vectorize texts and predict its rating '''
    model = load_models()
    texts = [examples['text']]
    if 'text_thresholded' in examples:
        for key in examples['text_thresholded']:
            texts.append(examples['text_thresholded'][key])
    vectorized_examples = model.vectorize_examples(texts)
    return model.predict(vectorized_examples).tolist()
