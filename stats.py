def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> int:
    corr_text = str.lower(text)
    char_dict = {}
    for char in corr_text: 
        if char in char_dict:
            char_dict[char] += 1     # Increment existing count
        else:
            char_dict[char] = 1      # Setting first occurrence

    return char_dict

def sort_on(item):
    return item["num"]

def sort_dictionary_by_value(d):
    items = [{"char": k, "num": v} for k, v in d.items()]
    items.sort(reverse=True, key=sort_on)
    return items