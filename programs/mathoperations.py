
import platform
def getsum():
    print("this is arithemtic operation")

def getsub():
    print("this is sub operation")

def getmul():
    print("this is multiplication")

def getdivision():
    print("this is division")

def getname():
     name = platform.machine()
     return name

# __name__ is predefined handler that holds __main__
#when we execute this program directly , below condition will be always True
# when this program is imported to other program, condition becomes False

getsum()
getsub()
getmul()
getdivision()