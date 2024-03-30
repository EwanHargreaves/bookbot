def main():
    frankenstein_path = "books/frankenstein.txt"
    read_book(frankenstein_path)

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        # print(file_contents)
        count_words(file_contents)

def count_words(text):
    words = text.split()
    print(f"book has {len(words)} words")


main()
