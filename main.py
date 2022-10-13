ip = "192.168.22.26/20"
# network = ...[x AND y]
#hostMin, hostmax = lowest ip possible, ...

sA = ip.split('.')
qTmp = sA[3].split('/')
sA[3] = qTmp[0]
ms = qTmp[1]
tm = 32-int(ms) #mask 1 len

print(sA, ms) # "192.168.22.26/20" -> "['192', '168', '22', '26'] 20"
bA = [format(int(v), '#010b')[2:] for v in sA]
#print(*bA, sep=".")
print(F"max címek: {2**(32-int(ms))-2}")
mask = ""
for i in range(32):
    if 32-i<tm:
        mask += '0'
    else:
        mask += '1'
    if i%8==0:
        mask += '.'
mask += '0'
mask = mask[2:]
#print(mask)

q = [int(sA[i]) & int("0b" + mask.split('.')[i], 2) for i in range(4)]
print("maszk: ", *[str(int("0b" + v, 2))+'.' for v in mask.split('.')], sep='')
print("network: ", end="")
print(*q, sep=".")
mi = ""

bbbbbbb = ''.join(bA)
épfeioewgú = mask.replace(".","")
for v in range(32):
    if épfeioewgú[v] == '1':
        mi += bbbbbbb[v]
    else:
        mi += '0'
mi = mi[:-1] + '1'
miA = [mi[i:i+8] for i in range(0, len(mi), 8)]
print("hostMin: ", end="")
print(*[int("0b" + v, 2) for v in miA], sep=".")

ma = ""
for v in range(32):
    if épfeioewgú[v] == '1':
        ma += bbbbbbb[v]
    else:
        ma += '1'
ma = ma[:-1] + '0'
maA = [ma[i:i+8] for i in range(0, len(ma), 8)]
print("hostMax: ", end="")
print(*[int("0b" + v, 2) for v in maA], sep=".")

broadcast = ""
for v in range(32):
    if épfeioewgú[v] == '1':
        broadcast += bbbbbbb[v]
    else:
        broadcast += '1'
broadcastA = [broadcast[i:i+8] for i in range(0, len(broadcast), 8)]
print("broadcast: ", end="")
print(*[int("0b" + v, 2) for v in broadcastA], sep=".")
