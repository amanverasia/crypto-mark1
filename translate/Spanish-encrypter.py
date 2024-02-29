from random import randint

plain_text = input('Orignal Text: ')
x1 = 1
x2 = 2

def random_n(n):
  range_start = 10**(n-1)
  range_end = (10**n)-1
  return randint(range_start, range_end)

def coding_ascii(text):
	crypt = ''
	for value in text:
	  if ord(value)<100:
	    crypt = crypt + '0' + str(ord(value))
	  else:
	    crypt = crypt + str(ord(value))
	return crypt
#coverting our values into numbers
plain_text_ascii = coding_ascii(plain_text)
#now starts the mathematical part
slope = random_n(len(plain_text_ascii))
#renaming slope as m and plain_text_ascii as c to make it better analogous to y = mx + c
m = slope
c = plain_text_ascii
y1 = m*x1 + int(c)
y2 = m*x2 + int(c)
pass1 = y1
pass2 = y2
#printing time
#print(f'Convereted ascii (c): {plain_text_ascii}\nLength: {len(plain_text_ascii)}')
# print(' ')
# print(f'Slope (m): {slope}')
if c[0]=='0': print('There was a 0 at the beginning.')
# print(' ')
# print(f'x1: {x1}')
# print(f'x2: {x2}')
print(f'Pass1 (y1): {pass1}')
print(f'Pass2 (y2): {pass2}')
