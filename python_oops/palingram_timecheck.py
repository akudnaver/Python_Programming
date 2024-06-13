from palingram import find_palingram
import time

start_time = time.time()
palingrams = find_palingram()
end_time = time.time()

print("Runtime for this program was {} seconds.".format(end_time - start_time))
