lst = []
while True :
  num = input("Enter a number: ")
  if num == "done":
    print("Max:",max(lst),"Min:",min(lst))
    break
    
  try:
    num = int(num)
    lst.append(num)
  
  except:
    print("invalid input")
    continue
  
