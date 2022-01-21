def add_time(start, duration, day = None):
  start_minute = int(start.split(":")[1][0] + start.split(":")[1][1])
  duration_minute = int(duration.split(":")[1])
  start_hour = int(start.split(":")[0])
  duration_hour = int(duration.split(":")[0])
  information = start.split(" ")[1]
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  minute_final = start_minute + duration_minute
  hour = start_hour + duration_hour
  if minute_final >= 60:
    hour += 1
    minute_final %= 60
  
  if hour >= 12 and information == "AM":
    if hour < 24:
      information = "PM"
    else:
      information = "AM"
      if day == None:
        information += " (next day)"
      else:
        day_final = days[(days.index(day.title()) + 1) % 7]
        information += ", " + day_final + " (next day)"
  elif hour >= 12 and information == "PM":
    information = "AM"
    if hour < 24:
      information += " (next day)"
    else:
      x = hour / 24 + 1
      if day == None:
        information += " (" + str(int(x)) + " days later)"
      
      else:
        y = days.index(day.title()) + int(x)
        if y > 6:
          y = int((x - 6 - days.index(day.title())) % 6) - 1
        day_final = days[y]
        information += ", " + day_final + " (" + str(int(x)) + " days later)"
  else:
    if day != None:
      information += ", " + day
      
  hour_final = hour % 12
  if hour_final == 0:
    hour_final = 12

  if len(str(minute_final)) < 2:
    return str(hour_final) + ":" + "0" + str(minute_final) + " " + information
  return str(hour_final) + ":" + str(minute_final) + " " + information