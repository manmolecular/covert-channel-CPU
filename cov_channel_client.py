import time
import psutil

# time.sleep(5)
# psutil.cpu_percent()

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


time.sleep(2)
message_bit = [] 
for i in range(80):
	if (psutil.cpu_percent() > 40):
		message_bit.append(1)
	else:
		message_bit.append(0)
	time.sleep(1)

print message_bit
message_bit = ''.join(str(x) for x in message_bit)
start = message_bit.find('01111011')
end = message_bit.rfind('01111101')
print message_bit
message_bit = message_bit[start:end + 8]
print message_bit
message_bit = [i for i in message_bit]

print message_bit
message  = (frombits(message_bit))
print message
