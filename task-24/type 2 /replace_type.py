#задание 2416
data = "AABECAEBECADA"
pairs = ['AB','AC','AD','EB','EC','ED']
for i in pairs:
    data = data.replace(i,"*")
for i in 'ABCDE':
    data = data.replace(i," ")
print(data)
data = data.split()
max_len = len(max(data,key=len))
print(max_len)