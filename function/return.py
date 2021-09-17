def print_dict(input_dict):
    for key, val in input_dict.items():
        print(key, val)


dict = {1: "one", 2: "two", 3: "three"}
print_dict(dict)


def get_first_last_word(text):
    words = text.split()
    return words[0], words[-1]


text = "hello, My name is Mike"
first, last = get_first_last_word(text)

print(first, last)
