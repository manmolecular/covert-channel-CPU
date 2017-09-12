from __future__ import print_function
import time
import psutil
import math


# time.sleep(5)
# psutil.cpu_percent()
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def one():
	start = int(time.time())
	while(int(time.time())-start != 1):
		1
		
def zero():
	time.sleep(1)

msg = "{{" + raw_input("Enter your secret message: ") + '}}'
msg_bit = (tobits(msg))
print (''.join(str(x) for x in msg_bit))
time.sleep(2)
for i in msg_bit:
	if(i):
		one()
	else:
		zero()
	print (i, end = '')
print ('')




