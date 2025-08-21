
def get_num_words(text):

    return len(text.split())


def count_characters(text):

    word_count = {}

    for w in text:
        lowered_c = w.lower()

        if lowered_c in word_count:
            word_count[lowered_c] += 1
        else:
            word_count[lowered_c] = 1

    return word_count




def sort_words(words_array):
    return sorted(words_array, key=lambda d: d["count"], reverse=True)