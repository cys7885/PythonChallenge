txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
a = ""

for c in txt:
	a += str(ord(c)) + ","
a = a[0:len(a)-1].split(',')

for i in range(len(a)):
	if a[i] == "32":
		a[i] = int(a[i])
		continue
	a[i] = int(a[i]) + 2
s = "".join([chr(c) for c in a])

print s
