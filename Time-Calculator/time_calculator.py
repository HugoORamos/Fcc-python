def add_time(start, duration, day=None):

  days = [
      "sunday",
      "monday",
      "tuesday",
      "wednesday",
      "thursday",
      "friday",
      "saturday"]
  
  
  
  # Separando minuto e hora e turno
  start = start.replace(":", " ")
  start = start.split(" ")
  start_h = int(start[0])
  start_min = int(start[1])
  meridiem = start[2]
  
  
  #convertendo pra formato 24h
  if meridiem == "PM":
      start_h += 12
  
  
  duration = duration.split(":")
  duration_h = int(duration[0])
  duration_min = int(duration[1])
  
  
  final_h = (start_h + duration_h)
  final_min = (start_min + duration_min)
  
  
  # Adicionando 1h caso soma dos minutos maior q 60
  if final_min > 59:
      final_min = final_min%60
      final_h += 1
  
  
  #botando o zero no final_min caso so tenha uma casa decimal
  if final_min < 10:
      final_min = (f"0{final_min}")
  
  
  # Contando os dias 
  days_passed =  final_h // 24
  
  
  # Garantindo que a hora não seja maior que 24
  if final_h > 24:
      final_h = final_h % 24
  
  if final_h > 12:
      meridiem = "PM"
      final_h -= 12
  
  elif final_h == 12:
      if meridiem == "AM":
          meridiem = "PM"
      elif meridiem == "PM":
          meridiem = "AM"
  
  else:
      meridiem = "AM"
  
  
  if final_h == 0 and meridiem == "AM":    
      final_h +=  12
  
  
  
  #day nao e nulo
  if day:
      day = day.lower()
      day_index = days.index(day)
      final_day_index = day_index + days_passed
  
  
      #para nao estourar o indice da lista de dias
      if final_day_index > 6:
          final_day_index = final_day_index % 7
  
  
      final_day = days[final_day_index]
      if days_passed == 0:
          new_time = (f"{final_h}:{final_min} {meridiem}, {final_day.capitalize()}")
          return new_time
  
      elif days_passed > 1:
          new_time = (f"{final_h}:{final_min} {meridiem}, {final_day.capitalize()} ({days_passed} days later)")
          return new_time
  
      elif days_passed == 1:
          new_time = (f"{final_h}:{final_min} {meridiem}, {final_day.capitalize()} (next day)")
          return new_time
  
  elif day == None and days_passed > 1:
      new_time = (f"{final_h}:{final_min} {meridiem} ({days_passed} days later)")
      return new_time
  
  elif day == None and days_passed == 1:
      new_time = (f"{final_h}:{final_min} {meridiem} (next day)")
      return new_time
  
  
  elif day == None and days_passed == 0:
      new_time = (f"{final_h}:{final_min} {meridiem}")
      return new_time