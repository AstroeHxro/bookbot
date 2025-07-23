from stats import word_count
from stats import letter_count


def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

book_contents = get_book_text('books/frankenstein.txt')

def main():

    
    word_count(book_contents)
    print(letter_count(book_contents))



main()
