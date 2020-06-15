#encrypting
from random import randint
text = input('Enter the text that you want to put: \n \n')
crypt = ''


def random_n(n):
  range_start = 10**(n-1)
  range_end = (10**n)-1
  return randint(range_start, range_end)

def converter(text):
	global crypt
	for value in text:
	  if ord(value)<100:
	    crypt = crypt + '0' + str(ord(value))
	  else:
	    crypt = crypt + str(ord(value))
	return crypt


crypt = converter(text)
print(f'\nThis is the converted form {crypt} and it has a length of {len(crypt)}\n')

num = random_n(len(crypt))
pass1 = num*1 + int(crypt)
pass2 = num*2 + int(crypt)
print(f'The random seed was: {num}\n')
if crypt[0]=='0':
  print('\nIt has a 0 at the start\n')
print(f'The two new keys are, \nPass1: {pass1} \n\nPass2: {pass2}')

with open('pass.txt', 'w') as f:
  f.write('Pass1 is: ' + str(pass1))
  f.write('\n')
  f.write('Pass2 is: ' + str(pass2))
f.close()
