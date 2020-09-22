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
		

# 轉換檔案
# 計算出每個人講了幾個字、貼圖和圖片
def convert(lines): # 將產生出的對話清單投入這個func
	person = None # 沒有預設值
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_img_count = 0
	viki_img_count = 0
	for line in lines:
		s = line.split(' ') # 字串分割，裡面用''作分割的標準，分割完後儲存成清單，再把它存到s的變數裡面
		time = s[0] # time是第一個
		name = s[1] # name是第二個
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_img_count += 1
			else: # 文字計數
				for msg in s[2:]:
					allen_word_count += len(msg) # len()算清單裡面的的長度
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_img_count += 1
			else:	
				for msg in s[2:]:
					viki_word_count += len(msg)
	print('allen說了', allen_word_count, '個字')
	print('viki說了', viki_word_count, '個字')
	print('allen傳了', allen_sticker_count, '個貼圖')
	print('viki傳了', viki_sticker_count, '個貼圖')
	print('allen傳了', allen_img_count, '個圖片')
	print('viki傳了', allen_img_count, '個圖片')
		#print(s)
	#return new # 回傳func


# 寫入檔案
def write_file(filename, lines): # 將lines傳進來
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') # 寫進去 + 換行符號


# main 是主要的執行func
def main(): 
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines) # 覆蓋上一個lines
	#write_file('output.txt', lines) # 寫入檔案，加上檔案
	
main() # 執行func


