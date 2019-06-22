''' Text processing functions using re'''
import re

def clean_text(text):
    ''' Deletes strange characters and spaces'''
    no_strange = re.sub(r'([^\s\w])*', '', text)
    no_newline = re.sub(r'([\n])+', ' ', no_strange)
    no_multispace = re.sub(r'([\s])+', ' ', no_newline)
    return no_multispace
