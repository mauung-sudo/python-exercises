xh = input ("Enter Hours: ")
xr = input ("Enter Rate: ")

try :
  fh = float(xh) 
  fr = float(xr) 
except :
  print("Error, please enter numeric input")
  quit()

if fh > 40.0 :
  bonus_hr = fh - 40.0
  bonus = bonus_hr *fr * 0.5
  xp =fh *fr + bonus
else :
  xp =fh *fr

print("Pay : " , xp)
