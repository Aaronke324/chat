#撰寫函式讀取txt檔
def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f: #encoding='utf-8-sig可去除\ufeff
		for line in f:
			lines.append(line.strip())
	return lines

#轉換文字
def convert(lines):
	new = []
	person = None #避免最一開始沒有對話者的狀況程式無法執行
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #若person有被設定出新值，才會執行下段程式
			new.append(person+":"+line)
	return new
	print(new)

#寫入檔案
def write_file(filename, lines):
	with open (filename, 'w', encoding='utf-8-sig') as f: 
		for line in lines:
			f.write(line + "\n")

def main():
	lines = read_file('input.txt')
	lines = convert(lines) #新的lines覆蓋原本從檔案中讀取的lines
	write_file('output.txt', lines)


main() #程式進入點