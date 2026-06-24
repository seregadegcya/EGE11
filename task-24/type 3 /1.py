# from string import digits, ascii_lowercase, ascii_uppercase
# alph = digits + ascii_lowercase + ascii_uppercase
# print(alph[:])
# from string import digits, ascii_uppercase
#
# data = "XZ1234AZZ"
# alph = digits + ascii_uppercase
# good = alph[:16]
# bad = alph[16:]
# for i in good:
#     data = data.replace(i, '*')
# for i in bad:
#     data = data.replace(i, ' ')
# # print(data.split())
# Текстовый файл состоит из десятичных цифр и
# заглавных букв латинского алфавита.
# Onределите в этом файле последовательность
# идущих подряд символов, представляющих собой
# запись максимального кратного пяти 15-ричного числа.
# В ответе запишите индекс (номер) последнего символа
# (последней значащей цифры), которой заканчивается
# запись этого числа в прилагаемом файле.
# Нумерация символов в текстовом файле начинается с нуля
# from string import ascii_uppercase, digits
# with open("22359.txt") as f:
#     data = f.readline()
# alpha = digits + ascii_uppercase
# good = alpha[:15]
# bad = alpha[15:]
# even = good[::5]
# string = ""
# cnt = max_len = 0
# for i in range(len(data)):
#     if string == "" and data[i] == "0":
#         continue
#     if data[i] in good:
#         string += data[i]
#     else:
#         string=""
#     if data[i] in even and max_len < cnt(string,15):
#         max_len = int(string,15)
#         index=i
# from string import ascii_uppercase, digits
# with open("22359.txt") as f:
#     data = f.readline()
# alpha = digits + ascii_uppercase
# good = alpha[:15]
# bad = alpha[15:]
# even = good[::5]
# left = 0
# substrings=[]
# for right in range(len(data)):
#     if data[right] in bad:
#         left = right + 1
#         continue
#     while data[left] == "0":
#         left += 1
#     if data[right] in even:
#         substring = data[left:right+1]
#         if substring:
#             substrings.append((substring, right))
# ans = max(substrings, key= lambda x:int(x[0],15))
# print(ans)
from string import ascii_uppercase, digits
# with open("22359.txt") as f:
#     data = f.readline()
alpha = digits + ascii_uppercase
good = alpha[:15]
bad = alpha[15:]
even = good[::5]
for i in range(len(data)):

for i in range(1,len(breaks)):
    left = breaks[i-1]+1
    right = breaks[i]
    part = data[left:right]
    while part and part[0] == '0':
        part = part[1:]
    for j in range(len(part)-1,-1,-1):
        if part[j] in even:
            number = part[:]
