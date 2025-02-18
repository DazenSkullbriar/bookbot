def sort_on(char_counts):
    return char_counts["count"]

def count_characters(text):
    char_counts = {}
    for char in text: 
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_string = file_contents.lower()
    result = count_characters(lowered_string)
    words = file_contents.split()
    wordcount = len(words)
    #print(wordcount)
    char_list = [] 
    for char, count in result.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document\n")

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

    print("--- End report ---")



if __name__ == "__main__":
    main()