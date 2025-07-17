import sys

from stats import get_word_count, get_char_total, sorted_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read() 
    return(file_contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path) 
    num_words = get_word_count(book_text) 
    char_count = get_char_total(book_text)
    sorted_chars = sorted_characters(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
