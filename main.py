from stats import get_num_words, get_char_distribution, sort_on, sort_distribution
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    dist = get_char_distribution(text)
    full_dist = sort_distribution(dist)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for item in full_dist:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

    # print(full_dist)
    

main()