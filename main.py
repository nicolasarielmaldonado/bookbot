
def main():
    book_report("./books/frankenstein.txt")
    
def book_report(filepath):
    book = getBook(filepath)
    word_count = count_words(book)
    character_count = count_characters(book)
    chars_sorted_list = chars_dict_to_sorted_list(character_count)

    print(f"--Begin report of {filepath}")
    print(f"{word_count} words found in the document" )
    print("")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}

    for char in text.lower(): 
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


def getBook(filepath):
    with open(filepath, "r") as f:
        file_contents = f.read()
        return file_contents
    
if __name__ == "__main__":
    main()