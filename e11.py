file = open("e5.txt")
count = 0
dd = dict()

for line in file:
  element = line.strip().split()
  #print(element)
  if line.startswith("From "):
    #print(element[2])
    date = element[2]
  
    if date not in dd:
      dd[date] = 1
    else: 
      dd[date] += 1

    count = count + 1
print(dd)
print(count)

