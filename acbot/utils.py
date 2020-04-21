import datetime

def time_of_day():
  now = datetime.datetime.now()

  if now.hour < 12:
      return 'AM'
  else:
      return 'PM'