# The yield statement acts as a checkpoint in the generator function. 
# When the caller requests the next value (by iterating over the generator or calling next() on it), 
# the function resumes execution immediately after the yield statement.

import time

def ft_progress(iterable):
    total = len(iterable)
    start_time = time.time()
    prev_time = start_time
    
    for i, item in enumerate(iterable):
        yield item

        current_time = time.time()
        elapsed_time = current_time - start_time
        percentage = (i + 1) / total * 100
        progress_bar = "=" * int(percentage / 5) + ">"
        eta = (total - i - 1) * (current_time - prev_time)
        prev_time = current_time

        print(f"ETA: {eta:.2f}s [{percentage:.0f}%][{progress_bar:<20}] {i+1}/{total} | elapsed time {elapsed_time:.2f}s", end="\r")


# # USAGE 1
# listy = range(1000)
# ret = 0
# for elem in ft_progress(listy):
# 	ret += (elem + 3) % 5
# 	time.sleep(0.01)
# print()
# print(ret)

# USAGE 2
listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
	time.sleep(0.005)
print()
print(ret)

