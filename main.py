from stats import word_count
from stats import letter_count
from stats import sorted_dict
import sys




def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents



def main():

    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_contents = get_book_text(sys.argv[1])

    
    

    num_of_letters = (letter_count(book_contents))
    
    
    

    print('============ BOOKBOT ============')
    print('')
    print(f'Analyzing book found at {sys.argv[1]}...')
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
