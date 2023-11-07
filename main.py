from bs4 import BeautifulSoup
from pathlib import Path
from methods.ngram_method import lang_ngram
import os

#
# HTML_PATH = Path(__file__).parent
# RU_HTML_PATH = HTML_PATH / Path(r'htmls/russian/russian.html')
# file = open(RU_HTML_PATH, 'r', encoding='utf-8')
# text = BeautifulSoup(file.read(), features='html.parser').get_text()
#
# # Используем метод get_text() для получения текста из HTML документа

folder_path = r"C:\eyazis_labs\eyazis2\htmls\russian"
file_list = os.listdir(folder_path)
print(file_list, 'fl')
l = list()
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        l.append(file_path)

print(l)


# # Выводим текст в консоль
# print(text.replace('\n', ' '))
#
# print(lang(text))
