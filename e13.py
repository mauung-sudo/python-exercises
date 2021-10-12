file = open("e8.txt")

counts = dict()
frequency = dict()
for line in file:
  words = line.strip().split()
  letterList = list(''.join(words))
  
  
  for letter in letterList:
    letter = letter.lower()
    counts[letter] = counts.get(letter,0) + 1

print(sorted([(v,k) for k,v in counts.items()],reverse = True))
  