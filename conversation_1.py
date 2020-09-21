# 將對話紀錄 input 檔案轉換成 output

# 讀取檔案
# 用 for 迴圈來讀取檔案，每一行都是一個 line
# 若出現 ufeff 這個編碼符號，用'utf8-sig'可以去掉
def read_file(filename): # 將檔名變成一個參數
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f: 
			lines.append(line.strip()) # strip()去掉換行符號
		return lines # 回傳func

def convert(lines): # 將產生出的對話清單投入這個func
	new = []
	person = None # 沒有預設值
	for line in lines:
		if line == 'Allen':
			person = 'Allen' # 遇到Allen，存成person
			continue # 遇到人名後，跳過，不要執行，遇到不是人名的，才加入清單
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # person有值的話，才加到清單裡面
		# 字串合併
			new.append(person + ': ' + line)
	return new # 回傳func

# 寫入檔案
def write_file(filename, lines): # 將lines傳進來
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') # 寫進去 + 換行符號


# main 是主要的執行func
def main(): 
	lines = read_file('input.txt')
	lines = convert(lines) # 覆蓋上一個lines
	write_file('output.txt', lines) # 寫入檔案，加上檔案
	
main() # 執行func


