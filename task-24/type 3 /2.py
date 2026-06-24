from string import digits, ascii_uppercase
data = "XZ1234AZZ"
alph = digits + ascii_uppercase
good = alph[:16]
cnt=max_len=0
for i in range(len(data)):
    if data[i] in good:
        cnt+=1
    else:
        cnt=0
    max_len = max(max_len,cnt)
print(max_len)
# current_len = 2
# for i in range(len(data)):
#     current_len += 1
#     if data[i] == data[i+1] == data[i+2] == '*'
#         current_len = 0
#     max_len = max(current_len, max_len)
# print(max_len)