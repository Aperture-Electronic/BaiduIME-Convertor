with open("cphrase.ini", encoding='utf-16le', mode = "r") as f:
	datas = f.readlines();

length = len(datas);

codes = [];
orders = [];
words = [];

for n in range(0, length):
	string = datas[n];
	if(string.find("=") == -1): continue;
	sp = string.split("=", 1);
	codes.append(sp[0])
	ow = sp[1].split(",", 1);
	orders.append(str(int(ow[0]) + 1));
	words.append(ow[1]);

count = len(codes);

with open("output.txt", encoding = "utf16", mode = "w") as f:
	for n in range(0, count):
		dat = orders[n] + "," + codes[n] + "=" + words[n];
		f.write(dat)


