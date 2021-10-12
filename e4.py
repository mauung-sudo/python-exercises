str = 'X-DSPAM-Confidence: 0.8475'  
index = str.find(":")
number = float(str[index+1:]) #index+1 being white space .... to the end
print(number)
print("type of number : ",type(number))


