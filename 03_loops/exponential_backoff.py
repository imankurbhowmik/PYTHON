import time

attempt = 0
max_attempts = 5
wait_time = 1

while attempt < max_attempts:
    print("attempt:", attempt + 1, "waiting for", wait_time, "seconds")
    time.sleep(wait_time)
    attempt +=1 
    wait_time *= 2