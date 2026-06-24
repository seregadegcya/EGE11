data = "AABECAEBECADA"
chars = 'AE'
left = right = 0
max_len = 0
while right < len(data)-1:
    if data[right] in chars and data[right+1] not in chars:
        right += 2
        current_len = (right - left)//2
    else:
        right += 1
        left = right
print(max_len)
