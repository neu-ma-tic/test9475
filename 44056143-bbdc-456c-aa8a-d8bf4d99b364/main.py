import time
import datetime

year = input()
month = input()
day = input()

end_time = datetime.datetime(year, month, d, 23+2, 59, 59,0)

def countdown(stop):
  while True:
      difference = end_time - datetime.datetime.now()
      count_hours, rem = divmod(difference.seconds, 3600)
      count_minutes, count_seconds = divmod(rem, 60)
      if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
          print("Good bye!")
          break
      print('The count is: '
            + str(difference.days) + " day(s) "
            + str(count_hours) + " hour(s) "
            + str(count_minutes) + " minute(s) "
            + str(count_seconds) + " second(s) "
            )
      time.sleep(1)

countdown(end_time)