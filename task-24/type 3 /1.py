# from string import digits, ascii_lowercase, ascii_uppercase
# alph = digits + ascii_lowercase + ascii_uppercase
# print(alph[:])
from string import digits, ascii_uppercase

data = "XZ1234AZZ"
alph = digits + ascii_uppercase
good = alph[:16]
bad = alph[16:]
for i in good:
    data = data.replace(i, '*')
for i in bad:
    data = data.replace(i, ' ')
print(data.split())