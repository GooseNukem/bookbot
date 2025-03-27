def word_count(book_string): 
    word_count = len(book_string.split())
    return word_count

def character_total(book_string):
    character_set = set()
    list_of_dicts = []
    book_string = book_string.lower()

    for i in book_string: 
        character_set.add(i)

    for i in character_set: 
        list_of_dicts.append({"Character": i, "Occurences": book_string.count(i)})
    return list_of_dicts

def sort_on(dict): 
    return dict["Occurences"]

# def sorted_list_characters(letter_counts):




