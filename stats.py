def get_word_count(text):
    words = text.split()
    total_words = len(words)
    return total_words

def get_char_total(text):
    text = text.lower()
    char_counts = {

    }
    for char in text:
        if char not in char_counts:
           char_counts[char] = 1
        else:
           char_counts[char] += 1
    return char_counts

def sort_on(item):
    return item["num"]

def sorted_characters(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(key=sort_on, reverse=True)
    return char_list