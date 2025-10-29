# This program should read the contents of a .txt file and output statistics on the contents.

from stats import count_words
from stats import count_characters
from stats import sort_dictionary_by_value
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        return text
    
def main():
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]
    word_count = count_words(get_book_text(filename))
    char_count = count_characters(get_book_text(filename))
    char_dict_sorted = sort_dictionary_by_value(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_dict_sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()