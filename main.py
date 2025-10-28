import sys
from stats import get_book_text, word_count, charater_count, character_count_report


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file = sys.argv[1]
    print("============ BOOKBOT ============")
    contents = get_book_text(file)
    count = word_count(contents)
    print("----------- Word Count ----------")
    print(f"Found {count} total words")

    report = character_count_report(charater_count(contents))
    print("--------- Character Count -------")
    [print(f"{x['char']}: {x['num']} ") for x in report]
    print("============= END ===============")


main()
