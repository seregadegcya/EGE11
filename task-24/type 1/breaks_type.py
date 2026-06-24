
with open("../files/16333.txt") as f:
    data = f.readline()
data = data.translate(str.maketrans('QRW123', 'aaa000'))
breaks = []
for mistake in range (1,len(data)):
    if data[mistake] == data[mistake-1]:
        breaks.append(mistake)
breaks.append(len(data)-1)
maxlen = 0
for i in range(1,len(breaks)):
    distance = breaks[i] - breaks[i-1]
    maxlen = max(maxlen,distance)
print(maxlen)