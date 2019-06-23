''' For testing '''
import controllers.model_controller as model_controller

model_controller.create_models()

'''
MODEL = model_controller.load_models()

DATASET = MODEL.get_dataset()
TITLES = MODEL.get_titles()
VOTES = MODEL.get_votes()

DATA = DATASET[0, 0:5]
EXAMPLES = TITLES[0:5]
LABELS = VOTES[0:5]

LABELS_CLASSIFIED = MODEL.predict(EXAMPLES)

print(DATA)
print(LABELS)
print(LABELS_CLASSIFIED)
'''