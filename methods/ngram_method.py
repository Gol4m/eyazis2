# -*- coding: utf-8 -*-
import json
from pathlib import Path
from nltk import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer

JSON_PATH = Path(__file__).parent
print(JSON_PATH)
RU_JSON_PATH = JSON_PATH / Path(r'resources/ngram/ru.json')
DE_JSON_PATH = JSON_PATH / Path(r'resources/ngram/de.json')
print(RU_JSON_PATH)

with open(RU_JSON_PATH, "r") as read_file:
    ru_profile = json.load(read_file)

with open(DE_JSON_PATH, "r") as read_file:
    de_profile = json.load(read_file)


def lang_ngram(text):
    vectorizer = CountVectorizer(analyzer='char',
                                 ngram_range=(3, 3),
                                 max_features=300)
    vectorizer.fit_transform(sent_tokenize(text))
    ngrams = vectorizer.get_feature_names_out()

    ru_dict = 0
    for i, ng in enumerate(ngrams):
        try:
            ru_dict += abs(ru_profile[ng] - i)
        except KeyError:
            ru_dict += 300  # max dist

    de_dict = 0
    for i, ng in enumerate(ngrams):
        try:
            de_dict += abs(de_profile[ng] - i)
        except KeyError:
            de_dict += 300  # max dist

    print(f'ru dist {ru_dict}, de dist {de_dict}')

    if de_dict < ru_dict:
        return 'Немецком'
    elif de_dict > ru_dict:
        return 'Русском'
    else:
        return 'Невозможно определить'

