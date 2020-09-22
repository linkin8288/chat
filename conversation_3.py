lines = []
with open('r3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

# 字串str也可以用清單分割法
for line in lines:
	s = line.split(' ')
	time = s[0][:5] # 大清單裡面再分割小清單
	name = s[0][5:]
	print(time)
	print(name)
	
	
	
