def num_sum(no1: int, no2: int, no3: int) -> int:
    if no1 == no2 == no3:
        a = 3*(no1 + no2 + no3)
    else:
        a = "Numerele nu sunt egale"
    return a


print(num_sum(1, 1, 1))

#VARIANTA 2
# no1 = 1
# no2 = 1
# no3 = 1
#
# suma_numere = no1 + no2 + no3
# # if suma_numere/3 == no1:
# #     print(3*suma_numere)
# # else:
# #     print("Numerele nu sunt egale")
#
# a = suma_numere*3 if suma_numere/3 == no1 else "Numerele nu sunt egale"
# print(a)
