def count_letters(phrase):
    count_dict = {}
    for letter in phrase:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    # Maior valor de par chave valor encontrado
    max_key_value = max(count_dict.items(), key=lambda x: x[1])
    return count_dict

phrase = "asdasdasda"
print(count_letters(phrase))
