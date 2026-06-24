#replace

# data = ("111AAAAA333333AAAA")
# data = data.translate(str.maketrans('13579', '*****'))
# while '***' in data:
#     data = data.replace('***', '** **')
# print(data)
#linear

# data = ("111AAAAA333")
# data = data.translate(str.maketrans('13579', '*****'))
# max_len = 0
# current_len = 2
# for i in range(len(data)):
#     current_len += 1
#     if data[i] == data[i+1] == data[i+2] == '*'
#         current_len = 0
#     max_len = max(current_len, max_len)
# print(max_len)
#window
# data = ("111AAAAA333333AAAA")
# data = data.translate(str.maketrans('13579', '*****'))
# left = 0
# max_len = 1
# for right in range(len(data)):
#     if data[right] == data[right+1] == data[right+2] == "*":
#         print(left,right)
#
#         left = right-1
#     max_len = max(max_len, right - left + 1)
# print(max_len)
#breaks
#replace
# data = 'CBAAAAABABABACBCBABAAA'
# pairs = ["AB","CB"]
# for i in pairs:
#     data = data.replace(i, '*')
# for i in "ABC":
#     data = data.replace(i, ' ')
# data = data.split()
# max_len = max(data,key = len)
# print(max_len)
# data = 'CBAAAAABABABACBCBABAAA'
# pairs = ["AB","CB"]
# i = 0
# cnt = 0
# max_len = 0
# while i < len(data)-1:
#     pair = data[i] + data[i+1]
#     if pair in pairs:
#         cnt +=1
#         i += 2
#         max_len = max(max_len,cnt)
#     else:
#         cnt=0
#         i +=1
# print(max_len)
# data = 'CBAAAAABABABACBCBABAAA'
# pairs = ["AB","CB"]
# left = right = 0
# while right < len(data):
#     pair = data[right] + data[right+1]
#     if pair in pairs:
#         lenght = (right-left)//2
#         max_len = max(lenght, max_len)
#         right+=2
#     else:
#         left = right
#         right += 1
# print(max_len)
data = 'CBAAAAABABABACBCBABAAA'
pairs = ["AB","CB"]
breaks = [0]
i = 0
while i < len(data)-1:
    pair = data[i]+data[i+1]
    if pair in pairs:
        i +=2
    else:
        breaks.append(i)
        i+=1
for i in range(1, len(breaks)):
    distance = breaks[i] - breaks[i - 1]
    max_len = max(max_len, distance)
print(max_len//2)

