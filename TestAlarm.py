import datetime
import time
import winsound

# Function to set the alarm
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now == set_alarm_timer:
            print("Time to Wake up!")
            # Use any sound file you like as alarm sound.
            winsound.Beep(800,10000)
            break

# Get the alarm time from the user
alarm_time = input("Set your alarm time in HH:MM 24 hour format:\n>> ")

# Check the input format
if len(alarm_time) == 5 and alarm_time[2] == ':':
    hour = alarm_time[0:2]
    minute = alarm_time[3:5]
    set_alarm_timer = f"{hour}:{minute}:00"
    print(f"Alarm is set for {set_alarm_timer}.")
    alarm(set_alarm_timer)
else:
    print("Invalid time format. Please use HH:MM in 24 hour format.")


