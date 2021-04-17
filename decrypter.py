pass1 = input('Pass1: ')
pass2 = input('Pass2: ')
x1 = 1
x2 = 2

def decoding_ascii(text):
	plain_text = ''
	for i in range(len(plain_text_ascii)):
		if(i%3==0):
			start = i
			end = i + 3
			plain_text = str(plain_text) + str(chr(int(plain_text_ascii[start:end])))
	return plain_text

zero_at_start = input('Was there a zero at the start? (y/n): ')

if(zero_at_start == 'y'):
	zero_at_start = True
else:
	zero_at_start = False

#converting all the variables into their mathematical form
y1 = int(pass1)
y2 = int(pass2)
m = (y2-y1)
c = int(y1 - m*x1)
plain_text_ascii = str(c)

if(zero_at_start):
	plain_text_ascii = '0' + plain_text_ascii

plain_text = decoding_ascii(plain_text_ascii)
#printing time
print(f'Slope (m): {m}')
#print(f'Convereted ascii (c): {plain_text_ascii}\nLength: {len(plain_text_ascii)}')
print(f'Orignal Text: {plain_text}')
