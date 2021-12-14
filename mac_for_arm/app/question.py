import random

import operate_english_words_file


def select_english_word(file_path, checker):
    """
    select randomly english word from csv file

    param
    --------------------
    file_path: str

    return
    --------------------
    english: str
    japanese: str
    """
    # english_words_file = operate_english_words_file.File(file_path)
    # i = random.randint(0, english_words_file.df.shape[0]-1)
    # english, japanese = english_words_file.df.iloc[i]['English'], english_words_file.df.iloc[i]['Japanese']
    # return english, japanese
    english_words_file = operate_english_words_file.File(file_path)
    english_words_counts = english_words_file.df.shape[0]
    while True:
        i = random.randint(0, english_words_counts-1)
        if len(checker) == english_words_counts:
            checker = 'reset'
            return 'すべての単語がでました', 'Answerを押してください', checker
        elif i in checker:
            continue

        checker.append(i)
        english, japanese = english_words_file.df.iloc[i]['English'], english_words_file.df.iloc[i]['Japanese']
        return english, japanese, checker


def select_english_word_for_memorize(file_path, i):
    """
    select in order english word from csv file
    return i + 1

    param
    --------------------
    file_path: str
    i: int
        index

    return
    --------------------
    english: str
    japanese: str
    i: int
    """
    english_words_file = operate_english_words_file.File(file_path)
    max_index = english_words_file.df.shape[0]
    english, japanese = english_words_file.df.iloc[i%max_index]['English'], english_words_file.df.iloc[i%max_index]['Japanese']
    i += 1
    return english, japanese, i


if __name__ == '__main__':
    pass