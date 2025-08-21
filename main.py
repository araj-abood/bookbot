from stats import get_num_words, count_characters, sort_words
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]


def main():
    

    content = get_book_text(file_path)
    num_of_words = get_num_words(content)
    characaters_count = count_characters(content)

    words_array = []
    for word in characaters_count:
        word_data = {"word": word, "count": characaters_count[word]}
        words_array.append(word_data)
    
    words_array = sort_words(words_array)

    print_ui(words_array, num_of_words)

def get_book_text(file_path):
    content = ""
    
    with open(file_path) as f:
        content = f.read()    
           
        return content


def print_ui(words_count, total_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for word_details in words_count:
        print(f"{word_details["word"]}: {word_details["count"]}")


main()
