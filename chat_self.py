def read_file(filename):
	lines = []
	with open(filename,'r',encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip().split())
	return lines

def search(text,lines):
	
	new = []
	for line in lines:
		if text in str(line):
			print (line)



if __name__ == '__main__':
	lines = read_file('歡聊天記錄.txt')
	text = input('輸入要搜尋的對話')
	lines = search(text,lines)
						