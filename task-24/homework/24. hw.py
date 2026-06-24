# Текстовый файл состоит не более чем из 106 символов и содержит только заглавные буквы
# латинского алфавита (A..Z).
# Определите максимальное количество идущих подряд символов,
# среди которых нет сочетания стоящих рядом букв P и R (в любом порядке).
# with open ("../files/1873.txt TXT ᐧ 977 KB.webloc") as f:
#     data = f.readline()
#     data = data.replace("pr", "p r").replace("rp", "r p")
#     answer= len(max(data.split(), key=len))
#     print(answer)
# with open ("../files/1873.txt TXT ᐧ 977 KB.webloc") as f:
#     data = f.readline()
# cur = 0
# max_len=0
# for i in range (len(data)-1):
#     if data[i]+ data[i+1] in ("pr","rp"):
#         cur = 1
#     else:
#         cur +=1
#         max_len = max(max_len,cur)
# print(max_len)
# екстовый файл состоит из арабских цифр (0, 1, …, 9).
# Определите максимальное количество идущих подряд символов в
# прилагаемом файле,
# среди которых нет символов 0, стоящих рядом.
# with open ("../files/2410.txt") as f:
#     data = f.readline()
#     data = data.replace("00", "0 0")
#     answer= len(max(data.split(), key=len))
#     print(answer)
# with open ("../files/2410.txt") as f:
#     data = f.readline()
# cur = 0
# max_len=0
# for i in range (len(data)-1):
#     if data[i]+ data[i+1] in ("00"):
#         cur = 1
#     else:
#         cur +=1
#         max_len = max(max_len,cur)
# print(max_len)
# Задание для домашней работы:
# Текстовый файл 2411.txt.txt состоит из арабских цифр (0, 1, …, 9).
# Определите максимальное количество идущих подряд символов в прилагаемом файле,
# среди которых нет символов 1 и 2, а также 1 и 3 стоящих рядом.
# with open("../files/2411.txt") as f:
#     data = f.translate(str.maketrans("123","aop"))
# while "ao" in data or "ap" in data:
#     data = data.replace("ao",'a o').replace("ap","a p")
# data = data.split()
# answer = max(data, key=len)
# print(answer)
# Текстовый файл состоит из символов, обозначающих десятичные цифры и заглавные буквы латинского алфавита.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# которые могут представлять запись чётного числа в двенадцатеричной системе счисления.
# В этой записи отсутствуют незначащие (ведущие) нули.
import sys
# from string import digits, ascii_uppercase
# with open("2422.txt") as f:
#     data = f.readline()
# good = digits + ascii_uppercase
# alph = digits + ascii_uppercase
# good = alph[:12]
# n="02468A"
# cnt=max_len=0
# for i in range(len(data)):
#     if data[i] not in good or data[i] == '0':
#         a=i
#         while a < len(data) and data[a] in good:
#             a+=1
#         cur_len = a-i
#         if data[a-1] in n:
#             max_len = max(max_len,cur_len)
# print(max_len)
from string import digits, ascii_uppercase

# data = "XZ1234AZZ"
# alph = digits + ascii_uppercase
# good = alph[:12]
# bad = alph[12:]
# n="02468A"
# for i in good:
#     data = data.replace(i, '*')
# for i in bad:
#     data = data.replace(i, ' ')
# data=data.split()
# max_len = 0
# from string import digits, ascii_uppercase
# with open("2422.txt") as f:
#     data = f.readline()
# good = digits + ascii_uppercase
# alph = digits + ascii_uppercase
# good = alph[:12]
# n="02468A"
# cnt=max_len=0
# for i in range(len(data)):
#     if cnt == 0 and data[i] == "0":
#         continue
#     if data[i] in good:
#         cnt+=1
#         if data[i] in n:
#             max_len=max(max_len, cnt)
#     else:
#         cnt=0
# print(max_len)
# from string import digits, ascii_uppercase
# with open("2422.txt") as f:
#     data = f.readline()
# alph = digits + ascii_uppercase
# good = alph[:12]
# bad=alph[12:]
# n="02468A"
# cnt=max_len=0
# for sym in bad:
#     data = data.replace(sym, " ")
# for element in data.split():
#     while element and element[0] == '0':
#         element = element[1:]
#     while element and element[-1] not in n:
#         element = element[:-1]
#     max_len=max(len(element), max_len)
# print(max_len)
# from string import digits, ascii_uppercase
# with open("2422.txt") as f:
#     data = f.readline()
# good = digits + ascii_uppercase
# alph = digits + ascii_uppercase
# good = alph[:12]
# n="02468A"
# left=max_len=0
# for right in range(len(data)):
#     if data[right] in good:
# Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита.
# Определите в этом файле последовательность
# идущих подряд символов, представляющих собой запись максимального чётного 14-ричного числа.
# В ответе запишите количество символов (значащих цифр в записи числа) в этой последовательности.
# from string import digits, ascii_uppercase
# with open("2424.txt") as f:
#     data = f.readline()
# alph = digits + ascii_uppercase
# good = alph[:14]
# n="02468AC"
# cnt=max_len=0
# for i in range(len(data)):
#     if data[i] in good:
#         cnt+=1
#         if data[i] in n:
#             max_len=max(max_len, cnt)
#     else:
#         cnt=0
# print(max_len)
# from string import digits, ascii_uppercase
# with open("2424.txt") as f:
#     data = f.readline()
# alph = digits + ascii_uppercase
# good = alph[:14]
# bad=alph[14:]
# n="02468AС"
# max_len=0
# for sym in bad:
#     data = data.replace(sym, " ")
# for element in data.split():
#     while element and element[-1] not in n:
#         element = element[:-1]
#     if element:
#         max_len = max(len(element), max_len)
# print(max_len)
