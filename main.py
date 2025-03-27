file_path_being_read = ""
import sys
from stats import word_count
from stats import character_total
from stats import sort_on

def get_book_text(path_to_file):
    file_path_being_read = path_to_file
    with open(path_to_file) as f:
        book_contents = f.read()
    return book_contents

def sort_on(dict):
    return dict["Occurences"]

def main(): 
    if len(sys.argv) != 2: 
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    book_contents = get_book_text(sys.argv[1])
    word_counter = word_count(book_contents)
    letter_counts = character_total(book_contents)
    print("========= BOOKBOT ===========")
    print(f"Analyzing book found at {file_path_being_read}")
    print("========= Word Count ========")
    print(f"Found {word_counter} total words")
    print("========= Character Count ========")
    letter_counts.sort(reverse=True, key=sort_on)
    
    for i in letter_counts: 
        print(f'{i["Character"]}: {i["Occurences"]}')
    


main()
        
    

