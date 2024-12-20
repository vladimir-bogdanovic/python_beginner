import time

user_input = input("Input time in seconds.")
time_in_seconds = int(user_input)

def countdown(t):
    while t:
        converted_time = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(converted_time[0], converted_time[1])
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

countdown(time_in_seconds)