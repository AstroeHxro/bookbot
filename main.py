from stats import word_count
from stats import letter_count
from stats import sorted_dict


def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

book_contents = get_book_text('books/frankenstein.txt')

def main():

    
    

    num_of_letters = (letter_count(book_contents))
    
    
    

    print('============ BOOKBOT ============')
    print('')
    print('Analyzing book found at books/frankenstein.txt...')
    print('')
    print('----------- Word Count ----------')
    print('')
    word_count(book_contents)
    print('')
    print('--------- Character Count -------')
    print('')
    sorted_chars = sorted_dict(num_of_letters)
    for item in sorted_chars:
        if item['char'].isalpha():
            print(item['char'] + ':', item['num'])
    print('')
    print('============= END ===============')




main()
