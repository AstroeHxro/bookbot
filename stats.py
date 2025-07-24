def word_count(book_contents):
   
    num_words = len(book_contents.split())
    print(f'Found {num_words} total words')




def letter_count(book_contents):
    
    num_of_letters = {}

    book_contents = book_contents.lower()

    for char in book_contents:

        if char in num_of_letters:
            num_of_letters[char] += 1
        else:
            num_of_letters[char] = 1
   

    return num_of_letters


def sorted_dict(num_of_letters):

    after_sort = []

    for char, num in num_of_letters.items():
        info = {'char': char, 'num': num}
        after_sort.append(info)
    after_sort.sort(reverse=True, key=in_order)
    return after_sort

def in_order(items):
    return items['num']




    



    



