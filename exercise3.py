import itertools

combinations_list = []
values_list = []
z = []

initial_dictionary = {"1": "abc", "2": "s", "3": "o", "4": "n", "5": "lm", "6": "jk", "7": "gi", "8": "def", "9": "abc"}

for keys, values in initial_dictionary.items():
    values_list.append(values)

print(list(itertools.product(*values_list)))


# z = []
# a = "abc"
# b = "c"
# for letter in a:
#     for letter2 in b:
#         x = zip(letter, letter2)
#         print(list(x))
#         z.append(list(zip(letter, letter2)))
#         print(z)

# print(z)

for string in initial_dictionary.values():
    combinations_list.append(string)

print(combinations_list)
