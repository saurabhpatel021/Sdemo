a=input("num of a=")                #take input from user
b=input("num of b=")                #take input from user
c=input("num of c=")                #take input from user
d=input("num of d=")                #take input from user
a=float(a)                          #convert into float
b=float(b)                          #convert into float
c=float(c)                          #convert into float
d=float(d)                          #convert into float

#sum=a+b+c+d
#print "sum="
#print sum


if a>1:
    print ("addition")
    print (a+b+c+d)
elif a>5:
    print ("multiplication")
    print (a*b*c*d)
elif a>10:   
    print ("division")
    print (a/b/c/d)
elif a>50:   
    print ("substraction")
    print (a-b-c-d)
else:
    print ("invalid")

raw_input()
