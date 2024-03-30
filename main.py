def main():
    book = "frankenstein"
    print(f"Begin Report of book: {book}\n")

    book_path = "books/" + book + ".txt"
    text = read_book(book_path)

    word_count = count_words(text)
    character_count = count_characters(text)

    print_results(word_count, character_count)


def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
    

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    char_dict = {}

    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    char_dict = dict(sorted(char_dict.items(), key = lambda item: item[1], reverse = True))
    return char_dict

def print_results(word_count, character_count):
    print(f"book has {word_count} words\n")

    for char in character_count:
        if char.isalpha():
            num = character_count[char]
            print(f"The character '{char}' appears {num} times")


main()
