import pandas as pd
import fasttext
from sklearn.model_selection import train_test_split
import re
from gensim.parsing.preprocessing import STOPWORDS
from gensim.parsing.preprocessing import remove_stopwords

pd.options.display.max_colwidth = 1000

# Создадим текстовые файля для обучения модели с лейблом и текстом
with open('train.txt', 'w') as f:
    for each_text, each_label in zip(train['headline'], train['is_sarcastic']):
        f.writelines(f'__label__{each_label} {each_text}\n')

with open('test.txt', 'w') as f:
    for each_text, each_label in zip(test['headline'], test['is_sarcastic']):
        f.writelines(f'__label__{each_label} {each_text}\n')

# Разделяем данные на обучающие и текстовые
train, test = train_test_split(df_headline, test_size = 0.2)

# Сохраним модель с оптимизированными гиперпараметрами и самой высокой точностью
model6.save_model('optimized.model')

def lang_nn(text):
    # Загружаем, сохраненную ранее модель
    model = fasttext.load_model("optimized.model")
    language = model.predict(text)
    if language == 'rus':
        return "Русском"
    elif language == 'deu':
        return "Немецком"
    return language



