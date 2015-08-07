i=0
while (i<4):                    #use for controling from 0 to 4 times
 t=input("enter temprature=")   #for user input
 t=int(t)                       #convert into integer
 i=i+1
 if t>=31 and t<35:             #start if...else if statement
  print("Sunny day")
 elif t>=35 and t<40:
  print("Warm day")
 elif t>=40 and t<50:
  print("hot day")
 else:
  print("Invalid")
