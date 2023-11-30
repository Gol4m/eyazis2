from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
import os
from bs4 import BeautifulSoup

LOCAL_PATH = "C:\\eyazis2"

class NeuralNetworkMethod:
    def __init__(self):
        labels = [*["deu"] * 3, *["rus"] * 3]
        self.__label_dict = {label: idx for idx, label in enumerate(set(labels))}
        document_dir = "C:\\eyazis2\\htmls\\rus_and_deu"
        file_list = os.listdir(document_dir)
        files_in_dir = list()
        for file_name in file_list:
            file_path = os.path.join(document_dir, file_name)
            if os.path.isfile(file_path):
                files_in_dir.append(file_path)
        training_texts = list()
        for file in files_in_dir:
            file_ = open(file, 'r', encoding='utf-8')
            text = BeautifulSoup(file_.read(), features='html.parser').get_text()
            training_texts.append(text)

        self.__vectorizer = TfidfVectorizer()
        training_input = self.__vectorizer.fit_transform(training_texts)
        training_output = [self.__label_dict[label] for label in labels]

        self.__classifier = MLPClassifier()
        self.__classifier.fit(training_input, training_output)

    def predict_language(self, text) -> str:
        test_input = self.__vectorizer.transform([text])
        lang = [lang for lang, idx in self.__label_dict.items() if idx == self.__classifier.predict(test_input)][0]
        if lang == "deu":
            return "Немецком"
        elif lang == "rus":
            return "Русском"
        else:
            return "Неизвестном"


detector = NeuralNetworkMethod()
lang = detector.predict_language("Großer Beispieltext auf Deutsch")
print(lang)

# from ftlangdetect import detect
#
#
# def lang_nn(text):
#     text = text.replace('\n', ' ')
#     language = detect(text=text, low_memory=False)
#     if language['lang'] == 'ru':
#         return "Русском", language['score']
#     elif language['lang'] == 'de':
#         return "Немецком", language['score']
#     else:
#         return "Неопределённом", str(0)
#
# print(lang_nn("Какой-то пример текста"))
