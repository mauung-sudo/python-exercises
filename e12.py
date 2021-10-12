fname = input("Enter file name: ")
try:
  file = open("e5.txt")
except:
  quit()

count = 0
dd = dict()
mm = dict()
hh = dict()

for line in file:
  word = line.strip().split()
  
  if line.startswith("From "):

    email = word[1]

    domainName = email.split("@")[1]
    hour = word[5].split(":")[0] 

   
   
    if hour not in hh:
      hh[hour] = 1
    else:
      hh[hour] += 1    
    
    if email not in dd:
      dd[email] = 1
    else:
      dd[email] += 1    

    if domainName not in mm:
      mm[domainName] = 1
    else:
      mm[domainName] += 1



print(dd)
print(mm)


print(sorted([(k,v) for k,v in hh.items()],reverse = False))
  
print("_________")

largest = None

# for key,value in dd.items():
  
#   if largest is None or value > largest:
#     largest = value
#     email = key
    
# print(email, largest)
print(sorted([(v,k) for k,v in dd.items()],reverse = True)[0])

