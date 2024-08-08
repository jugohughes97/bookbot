def main(): 
    # with open("books/frankenstein.txt") as f:
    #     file_contents = f.read()
    #     words = 0
    #     for n in file_contents.split():
    #         words += 1
    
    book = "books/frankenstein.txt"
    words = word_count(read_book(book))
    letter_dict = char_count(read_book(book))
    print(f"{book} contains {words} words")
    print(f"{book} has the following letter counts: \n {letter_dict}")

def read_book(path):
   
    return open(path).read()


def word_count(text):
    
    words = 0
    for n in text.split():
        
        words += 1
    
    return words

def char_count(text):
    lower_text = text.lower()
    letters = "qwertyuiopasdfghjklzxcvbnm"
    # letters = str(sorted(letters))
    letter_dict = {}
    for letter in letters:
        letter_dict[letter] = lower_text.count(letter)
    
    return letter_dict
main()