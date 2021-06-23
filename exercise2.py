initial_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def remove_number(num_list: list) -> (list, list):
    a = []
    for i in range(3):
        while len(num_list) != 0:
            if len(num_list) >= 4:
                for number in num_list[::3]:
                    a.append(number)
                    num_list.remove(number)
                    print(num_list)     # can be removed
                    print("removed", a[-1])
            else:
                for number2 in num_list:
                    a.append(number2)
                    num_list.remove(number2)

        i += 1

    return num_list, a


remove_number(initial_list)

