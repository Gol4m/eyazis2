# -*- coding: utf-8 -*-
from collections import Counter

russian = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
           'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
           'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

deutsch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']


def lang_alph(text: str):
    counter = Counter(text.lower())

    russian_count = 0
    for letter in russian:
        russian_count += counter[letter]

    deutsch_count = 0
    for letter in deutsch:
        deutsch_count += counter[letter]

    if russian_count > deutsch_count:
        return "Русском"
    elif russian_count < deutsch_count:
        return "Немецком"
    else:
        return "Unable to recognize"

