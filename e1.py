xh = float(input ("Enter Hours: "))
xr = float(input ("Enter Rate: "))
if xh > 40:
  bonus_hr = xh - 40.0
  bonus = bonus_hr * xr * 0.5
  xp = xh * xr + bonus
else :
  xp = xh * xr

print("Pay : " , xp)
