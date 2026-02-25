# every process/subprocess contains system calls

def display(a,b):
    c = a + b
    return c
total = display(10,20)
print(total)

# pythonic way
# lambda is the replacment of single liner function
#syntax: functioname = lambda varibles:expression

display = lambda a,b : a + b
total = display(10,20)
print(total)

#length of string
getlength = lambda x : len(x)
print(getlength("python"))

getupper = lambda x: x.upper()
print(getupper("python"))

# max of 2 numbers
getmax = lambda a,b: a if a > b else b
print(getmax(10,20))

#even or odd
checkeven = lambda x: "even" if x % 2 == 0 else "Odd"
print(checkeven(9))

# positive negative or ero
sign = lambda x : "positive" if x > 0 else  "negative" if x < 0 else "zero"
print(sign(-5))


student = {"name":"rita","age":20}
getage = lambda d : d['name']
print(getage(student))


getsum = lambda *args : sum(args)
print(getsum(10,20,30,40,50,60,70,80,90,100))


def getlen(z):
    return len(z)

#length of string
getlength = lambda x : getlen(x)
print(getlength("python"))