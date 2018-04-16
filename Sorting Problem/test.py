

import time


t0 = time.time()
x = 0
for i in range (1 , 1000000,1):
	x = x+i

t1 = time.time()


print ((t1-t0)*1000000)
