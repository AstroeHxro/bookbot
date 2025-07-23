def word_count(book_contents):
   
    num_words = len(book_contents.split())
    print(f'{num_words} words found in the document')




def letter_count(book_contents):
    
    num_of_letters = {}

    book_contents = book_contents.lower()

    for char in book_contents:

        if char in num_of_letters:
            num_of_letters[char] += 1
        else:
            num_of_letters[char] = 1
   

    return num_of_letters





