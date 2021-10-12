def computepay(hours,rate):
  if hours > 40:
    bonus_hr = hours - 40.0
    bonus = bonus_hr * rate * 0.5
    xp = hours * rate + bonus

  else :
    xp = hours * rate

  print("Pay : " , xp)

computepay(float(input ("Enter Hours: ")), float(input ("Enter Rate: ")))
