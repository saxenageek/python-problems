import time
import sys

sys.stdout.write("Enter starting number to print sequence and press Enter (will go till 0) : ")
n = input()

for l in xrange(n, -1, -1):
  sys.stdout.write(str(l) + " ")
  sys.stdout.flush()
  time.sleep(1)
