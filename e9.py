file = open("e5.txt")
count = 0

for line in file:
  element = line.strip().split()
#  print(element)
  if line.startswith("From "):
    print(element[1])
    count = count + 1
print(count)

