################ numbeers
for i in range(1,10,2):   #range(start,stop,step) is a builtin function
    print(i)

for i in range(10,0,-1):
    print(i)

######################### iterating string
name = "python"
for char in name:
    print(char)

####################### iterating list
alist = [10,20,30,40,50,60,70]
for value in alist:
    print(value)

########################### iterating tuple
atup = (10,20,30,40)
for value in atup:
    print(value)

###################### iterating dictionary
book = {"chap1":10 ,"chap2":20}
for key in book.keys():
    print(key)

for value in book.values():
    print(value)

for k,v in book.items(): # book.items() : [("chap1",10),("chap2":20)]
    print(k,v)