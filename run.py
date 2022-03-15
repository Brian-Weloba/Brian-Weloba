import time

ts= time.time()
print(ts)

file = open("time.txt", "w")
file.write(str(ts))
file.close()