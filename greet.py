from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H%M")
formatted_time = int(current_time)

name = input("Enter Your Name: ")

if formatted_time >= 0 and formatted_time < 1200:
    print("Good Morning", name)
elif formatted_time >= 1200 and formatted_time <= 1800:
    print("Good Afternoon", name)
elif formatted_time > 1800 and formatted_time < 2400:
    print("Good Night", name)