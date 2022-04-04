import string
import base64
import random
	

for x in range(100):

			result = "mfa." + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(84))

			f = open("token.txt", "a")

			f.write(result + '\n')
		
	

for x in range(100):

			first = "OTQ0Mj" + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(18))
			sec = "Y" + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(5))
			thrd = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(27))

			result = first + '.' + sec + '.' + thrd

			f = open("token.txt", "a")

			f.write(result + '\n')