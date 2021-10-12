file = open("e5.txt")
count = 0

for line in file:
  count = count+1
  str = line.rstrip()

  print(str.upper())
print(count)