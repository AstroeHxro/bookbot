magic_words = "abracadabra"



def magic_counter(magic_words):
    counter = {}

    for char in magic_words:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    print(counter)


magic_counter(magic_words)