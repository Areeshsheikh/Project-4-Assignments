import time
def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)       #minutes  & seconds are calculated
        time_format = '{:02d}:{:02d}'.format(mins, secs)      #MM & SS formate
        print(time_format, end='\r')
        time.sleep(1)     #delay
        seconds -= 1
    print("00:00 \n Time's Up!")


#user input for timer
total_seconds = int(input("Enter time in seconds for countdown: ")) 
countdown_timer(total_seconds)    