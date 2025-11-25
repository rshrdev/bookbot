import sys
from stats import get_word_count, get_char_count, get_sorted

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():

    if len(sys.argv) != 2:
        
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:

        book_text = get_book_text(sys.argv[1])
        char_count = get_char_count(book_text)
        word_count = get_word_count(book_text)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        for i in get_sorted(char_count):
            
            if i["char"].isalpha():

                print(f"{i["char"]}: {i["num"]}")

        return

main()