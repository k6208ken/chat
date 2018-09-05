def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def covert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0 
	allec_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]		
		if name == 'Allen':
			if s[2] == '貼圖':
				allec_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:	
					allen_word_count += len(m) 
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:	
					viki_word_count += len(m)
	print('Allen說了{}個字,傳了{}個貼圖,{}張圖片'.format(allen_word_count,allec_sticker_count,allen_image_count))	
	print('Viki說了{}個字,傳了{}個貼圖,{}張圖片'.format(viki_word_count,viki_sticker_count,viki_image_count))


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('-LINE-Viki.txt')
	lines = covert(lines)
	# print(lines)
	#write_file('output.txt', lines)

main()